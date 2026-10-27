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

The proof is analytic and appears in `RESULT.md`. The independent diagnostics in `verification.py` require only Python 3 and `mpmath>=1.3`. In the same directory execute `python verification.py`.

The script reports `PASS 78 quadrature, asymptotic, and derivative-sign checks`. It compares the product-gamma moment formula with numerical integration of the Bessel density, the stationary radial density with a distinct exponential-age integral of the transient kernel, its small-radius normalization and the derivative signs and unique mode in several subcritical, critical and supercritical parameter choices. In the exact theorem, the critical mode distinction holds for *all* \(d\geq3\) and \(\alpha>0\), not just these numerical choices.

The key symbolic identities are direct differentiation of \(Y=R^{\alpha+2}/[\kappa(\alpha+2)^2]\), the gamma Laplace transform, the Bessel integral for a gamma product, and the Riccati equation for \(h(z)=zK_{\nu-1}(z)/K_\nu(z)\). The generator reduction, Poisson renewal argument and Riccati monotonicity are proved in full in `RESULT.md`; numeric checking does not certify these identities universally. All source-dependent originality comparisons have residual literature risk, and no independent scientific audit has been performed.
