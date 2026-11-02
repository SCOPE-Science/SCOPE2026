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

# Reproduction and limits

Execute `python3 checker.py` with a standard Python 3 interpreter in the directory containing the research files. The checker uses only the standard library (`fractions` and `random`), produces `PASS 14500 exact-rational assertions`, and covers the exact Wardrop route costs, quadratic gap identities, finite-support moment inequality checks, sharp equality witnesses, and opposite-sign first-two-moment constructions. Analytical proof is in RESULT.md; finite computation is not exhaustive over all demand laws and is not used as the infinite-dimensional argument.

The analysis assumes exact normalized link latencies, nonatomic route choice conditioned on the realized demand, a costless shortcut, and finite demand second moment. No independent audit or field-data validation has been performed.
