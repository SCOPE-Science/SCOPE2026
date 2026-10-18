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

The independent executable `check.py` was run using Python, NumPy and SciPy; 218 numerical assertions passed. It evaluates the Fourier cosine kernel by numerical quadrature without invoking its closed-form transform; tests reconstruction after forward generation from distinct and equal rates across three independent mechanical parameter sets; tests strict/attained boundary cases; evaluates finite-chain covariance via a matrix Lyapunov equation for chain lengths \(22\) and \(40\); and checks convex boundary formulas. Finite-chain cross-checks use Gaussian colored wall surrogates *only for stationary covariances*, for which their matching two-time force kernel is sufficient.

The all-parameter proof is analytic: the Fourier kernel is transformed to a geometric sequence, a strictly convex function gives a monotone rate-imbalance map for fixed measured variance, and explicit inverse formulas recover the rates. There is no claim of exhaustive numerical enumeration of positive real rates. The upper admissibility boundary corresponds to a rate tending to infinity; it is not attained by finite rates.

The available source comparison inspects arXiv:2307.06127v3, Section 4.2 and Appendix B; arXiv:2210.09035; and arXiv:2404.00615. Priority is unverified independently and the possibility of a stronger implicit general inverse-moment result remains. The result concerns ideal infinite-chain stationary covariances, with no finite-data performance guarantee.
