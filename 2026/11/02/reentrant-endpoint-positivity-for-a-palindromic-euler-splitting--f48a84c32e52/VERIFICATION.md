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

Run `python verify.py` with `sympy` installed. The standalone script symbolically verifies the exact three-factor matrix and checks the necessary-and-sufficient criterion on 6,006 selected timesteps and rate pairs. Expected output: `VERIFY_OK: exact symbolic matrix and 6006 endpoint sign comparisons`.

These finite tests are corroborative, not the basis of the universal assertion. The analytic proof in `RESULT.md` checks both necessity and sufficiency for every positive rate pair and every nonnegative timestep. Equality endpoints are included. No independent external validation has been performed.
