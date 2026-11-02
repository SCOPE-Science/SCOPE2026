---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run `python3 verify_js.py` in a standard Python installation. It computes the exact finite binomial formula from the theorem with `fractions.Fraction`, bounds every natural logarithm above and below by a rational arctanh series with an explicit geometric tail, checks positivity of the interval at \(m=1,2\) and negativity at \(m=3,4\) for \(t=1/10\). Its recorded stdout is embedded as `verification_output.txt`.

The analytical proof in `RESULT.md` establishes the small-parameter expansion and large-block sign for all \(0<t<1\); the checker does **not** certify all real parameters, the limiting argument or historical priority. No independent audit has been performed.
