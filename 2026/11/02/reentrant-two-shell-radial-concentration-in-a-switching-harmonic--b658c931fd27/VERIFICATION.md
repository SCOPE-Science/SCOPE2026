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

The accompanying source is `verify.py` (Python 3; requires the SymPy and SciPy packages). Run `python verify.py`. It checks the exact algebra of the limiting logarithmic derivative, the quadratic discriminant and endpoint evaluations, the effective-stiffness/gamma-mixture Jacobian, gamma-mixture normalization at six switching ratios, the analytic sign patterns for four regimes, and the finite-dimensional conditional-chi density derivative at four specified radii for \(\alpha=0.1\), \(d=100\).

The critical infinite-dimensional claims are proved in `RESULT.md`: the stationary Gaussian mixture is normalized explicitly, the strong law gives the radius limit, the exact quadratic controls its critical points, and local \(C^1\) convergence of the radial densities supplies the eventual finite-dimensional sign pattern. Finite quadrature is not treated as proof for all dimensions or parameters.

Only the six-parameter on/off model with positive equal switching rates is addressed. No finite-dimensional sharp mode boundaries, explicit \(d_0(\alpha)\), or results with residual confining force during off periods are verified. Independent scientific and publication-priority assessment has not been performed.
