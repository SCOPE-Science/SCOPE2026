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

# Reproducibility checks

Run `python checks/verify_coefficients.py` with Python 3 and SymPy. It symbolically differentiates the exact Lyapunov function and verifies the one-turn radius coefficient, original-time period coefficient, and their logarithmic-phase ratio. A finite numerical sanity check was also run at two small radii; it is not proof of an infinite-time limit.

The global boundedness and LaSalle deductions, and the summation of return-map error bounds, are mathematical arguments stated in `RESULT.md`; no finite symbolic or numerical check can certify them in isolation. No independent audit has been performed.
