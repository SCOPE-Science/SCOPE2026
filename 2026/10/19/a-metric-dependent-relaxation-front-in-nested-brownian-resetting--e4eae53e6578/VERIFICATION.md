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

Run `python verification/check.py` with NumPy and SciPy. The numerical script contains 53 deterministic comparisons: exact incomplete-gamma transport formula versus independent midpoint-gamma quantile quadrature; fixed-window normal-overshoot scaling; total-variation density integration at critical depth; and macroscopic-front checks for both sides of the transition.

The analytic proof in RESULT.md supplies the unbounded-\(n\) and all-real-\(z\) claims, relying on gamma central limit and Chernoff bounds, \(L^1\) normal-density Taylor remainder estimates, Scheffé convergence and one-dimensional optimal-transport ordering. The numerical tests do not establish infinite limits or all-parameter coverage. NumPy/SciPy versions can change floating-point behavior; tolerances are indicated in the source.

The finite-time Gaussian-mixture identity is taken from Britton et al., arXiv:2609.25252v1 equation (2.10). The exact Wasserstein formula and critical-metric limits are the claims independently derived in RESULT.md. There is no external independent audit.
