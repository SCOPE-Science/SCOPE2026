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

# Reproducible verification

The standalone script `verify.py` requires Python 3 and its standard library. Run `python3 verify.py` from the directory containing this file and that script.

The executed script passed 252 exact-rational instances of the perpendicular Rayleigh-product identity; 870 exhaustive finite-grid checks of the strict rearrangement lower bound; 35 numerical checks of the explicit beta-to-log CDF transformation; 21 midpoint-quadrature comparisons of bias, orthogonal variance, and iid variance; and six small-spectral-gap leading-coefficient tests. No external data or numerical package is required.

These checks are regression and falsification aids. Exhaustive finite-grid rearrangement is not a proof for arbitrary continuous couplings; that result depends on the analytic rearrangement argument in `RESULT.md`. Numerical quadrature is not exact integration; the exact variance laws depend on absolutely convergent Fourier series and Parseval. Neither test set establishes priority against inaccessible literature.
