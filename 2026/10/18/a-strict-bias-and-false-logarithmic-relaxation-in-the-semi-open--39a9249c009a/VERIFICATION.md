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

# Reproducibility and mathematical boundaries

Run `python verify.py` using Python with NumPy, SciPy, SymPy installed. The supplied script was executed successfully and reported:

- Symbolic verification of the Poisson relaxation-area identity and both Dirichlet endpoint conditions.
- Comparison of twenty continuum sine-series values against an independent finite-difference Dirichlet heat propagator at four times and five positions.
- Finite-grid checks of shortcut undershoot, the analytic upper envelope, and the sharp \(t^{-1}\) late-time coefficient.
- Five independently summed exact relaxation-area series agreeing with the cubic formula.

The strict all-time sign is **analytical**, from the heat residual \(F H'/H^2<0\) and positivity of the Dirichlet heat kernel; the late-time logarithm follows from the indicated Taylor coefficient, not computational extrapolation. The exact area follows from the uniquely solved Dirichlet Poisson equation. No finite experiment certifies an infinite statement. Only the continuum semi-open scaling model is covered. Independent external audit has not been performed.
