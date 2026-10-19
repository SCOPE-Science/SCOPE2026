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

The full proof of the limiting formula is in RESULT.md, including the mixing bound and dominated-convergence justification. The standalone script `checker.py` runs without accessing external data: `python checker.py`. It uses NumPy and SciPy to solve three finite-dimensional Poisson equations and integrate the normalized population dynamics, with a transformed mass coordinate to avoid catastrophic cancellation near carrying capacity. It prints a final `PASS` after the linear residual checks and numerical time-asymptotic comparisons.

Numerical consistency is not an independent audit or a substitute for infinite-time analysis. No statistical identifiability, noise robustness, or discretization error bound is asserted.
