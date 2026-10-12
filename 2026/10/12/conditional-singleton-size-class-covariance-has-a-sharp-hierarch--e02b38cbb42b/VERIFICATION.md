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

The accompanying `verify.py` uses only the Python standard library. Run `python verify.py` to reproduce three independently counted finite moments and their covariance in every set partition through eight points, with exact rational arithmetic. Further tests compare the conditional covariance at three growing sizes with the saddle asymptotic for selected interior block densities and verify the positive roots and their ordering by bisection. The program reports 270 passed checks.

The source of the infinite theorem is the exact conditional generating function, the analytic saddle-point mixed derivative, and the strict convexity and monotonicity calculations in the proof. Neither the finite arithmetic nor numerical root-finding proves an infinite claim. No assertion is made for critical densities or growing block-size index. Independent audit has not been performed.

