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

# Verification and reproducibility

Run `python odd_regular_prism_verify.py` with Python 3 and the standard library. Actual execution completed with `ALL_CHECKS_PASSED`, including five direct edge-crossing Monte Carlo instances with 50,000 orientations each, independent midpoint angular quadrature of the analytic probability formula, and three numerical large-order checks. The exact finite proof and strict optimizer argument are in `RESULT.md`. These numerical tests do not independently certify all mathematical statements. Independent audit has not been performed.
