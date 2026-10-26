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

# Reproducibility and limits
Run `python verify.py` in a Python 3 standard-library environment. The verifier constructs the actual graph's synchronous chip update without assuming firing phases. It exhausts the naturally confined nonnegative chip box for the nine parameter pairs (1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), totalling 729,348 labelled configurations, and independently compares with both the phase sum and exact factorial formula. It then tests all 121 ordered shore-size pairs from 1 through 11 by both integer formulas. Output is recorded verbatim in `verification_output.txt`.

The general all-size theorem and Gaussian joint asymptotic depend on the mathematical proof in RESULT.md, not on numerical extrapolation. No independent external audit has been performed.
