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

# Reproducibility

Run `python3 verify.py` with a stock Python 3 installation. It uses only the standard library, constructs rational-polynomial coefficients through degree 14, verifies their two-adic lower-bound margins, independently computes integer coefficients for all five exceptions and forty high-valuation parameter tests, and checks the Legendre forbidden shape.

The complete infinite proof is the coefficient-polynomial congruence together with the parity and unit classification; finite test cases are not substituted for that argument. The output line `VERIFY_OK` indicates the embedded certificate tests completed successfully. Scientific independence has not been assessed.
