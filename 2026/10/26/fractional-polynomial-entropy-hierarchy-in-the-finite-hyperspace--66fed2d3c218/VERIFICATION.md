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

# Reproduction and proof boundary

Run `python3 checker.py` using standard Python 3. The output is embedded verbatim as `checker_output.txt`. The checker uses exact `fractions.Fraction` for the finite height and separation-time comparisons at exponent two; it uses floating-point trigonometry only for confirming selected chord inequalities.

The universal statements for every real exponent greater than one, every positive finite layer, all orbit horizons, and the complete compact hyperspace are proved analytically in `RESULT.md`, specifically through the consecutive-gap asymptotic, the upper spanning product bound, the separated-radius construction, and the quotient metric. Finite numerical tests are not infinite proofs. No external independent audit has been performed.
