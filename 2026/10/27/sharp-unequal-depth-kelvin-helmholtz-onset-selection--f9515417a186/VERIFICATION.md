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

# Verification and limits

The included `verify.py` uses NumPy, SciPy and mpmath, and can be run with `python verify.py`. It performs randomized comparisons of the full two-layer temporal discriminant and transformed threshold, independent scalar optimization of its finite-wavenumber minimizers, sampled monotonicity checks and arbitrary-precision calculations of the edge scaling. It passed 239 randomized onset/discriminant trials and 9 high-precision critical-scaling cases in the supplied environment.

The all-parameter proof is analytic: the positive spectral expansion of the weighted hyperbolic-tangent kernel and its covariance derivative give a strictly increasing critical parameter, with exact endpoint values and expansion coefficients. Finite tests cannot certify an infinite-dimensional spectral assertion, establish novelty, or replace the proof. Independent audit has not been performed. The closest literature already gives the general forward dispersion and onset minimization; exact uniqueness, the sharp unequal-depth boundary, and the critical expansion are the assessed additional claims.
