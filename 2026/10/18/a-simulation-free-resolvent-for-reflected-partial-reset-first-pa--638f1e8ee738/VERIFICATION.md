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

# Reproduction
Run `python verify.py` with NumPy and SciPy. The test computes oscillatory Fourier integrals with 20–60 product factors, compares mean hitting times at three starting positions and three negative multipliers with an independently discretized two-sided backward equation, checks a conservative analytical series bound, and recovers the standard fixed-origin reset limit. The exact theorem holds for all \(-1<a<0\); a finite computational grid does not prove it. The error estimate in the result concerns term truncation, not quadrature discretization.
