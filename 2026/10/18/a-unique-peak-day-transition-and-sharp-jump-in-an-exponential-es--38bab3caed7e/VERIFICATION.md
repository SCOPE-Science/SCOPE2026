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
# Reproduction and scientific limits

Run `python3 VERIFY.py` from the same directory as `RESULT.md`. It uses only standard-library `decimal` and `fractions`, outputs 3052 passed arithmetic assertions, the critical root, the critical transmission value and both one-sided limits. The rational checks prove the specified endpoint first-two-step arithmetic; the decimal assertions sample parameters and localize the root numerically. Universal monotonicity and infinite-tail peak exclusion are justified instead by explicit inequalities in the proof. The executable does not purport to certify originality or the independence of a review.
