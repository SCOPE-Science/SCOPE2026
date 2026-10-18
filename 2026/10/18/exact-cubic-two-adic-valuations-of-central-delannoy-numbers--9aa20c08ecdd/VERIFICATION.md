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
# Verification

Run `python3 artifacts/verify.py` using the Python standard library. The standalone script exactly reconstructs the rational polynomial coefficients for both exceptional heights, verifies their normalized coefficient parities, checks a 2-adic cancellation to finite precision, and independently tests Delannoy values and the reflection law. The completed output is preserved in `artifacts/verification_output.txt`. Finite tests supplement the uniform proof in RESULT.md and do not imply an infinite identity by themselves. Independent validation has not been performed.
