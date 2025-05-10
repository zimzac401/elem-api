from flask import Flask, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/stoic-idea", methods=["GET"])
def get_idea():
    prompt = (
        "Give a short, original Stoic reflection to remind someone that life is temporary. "
        "Make it calm, deep, and suitable for daily meditation."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=80,
            temperature=0.7,
        )
        idea = response.choices[0].message.content.strip()
        return jsonify({"idea": idea})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
