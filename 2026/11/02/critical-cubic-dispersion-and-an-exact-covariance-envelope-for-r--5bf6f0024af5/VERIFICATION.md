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

# Reproducibility and verification

Run `python checks/verify.py` with Python 3 and the standard library. It checks the exact finite method-of-steps response across multiple delays, the linear-delay equation at regular test times, and three deterministic-quadrature variance intervals. It reports the number of assertions. The scientific proof uses a global Volterra comparison and Gaussian-process tightness, not extrapolation from finite checks. Independent scientific audit has not been performed.
