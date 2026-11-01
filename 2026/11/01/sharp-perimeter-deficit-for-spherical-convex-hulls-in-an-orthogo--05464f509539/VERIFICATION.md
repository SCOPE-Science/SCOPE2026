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
# Reproducibility and exact limits

Run `python3 verify.py` with Python 3.10+ and no external dependencies. The checker evaluates the exact finite-\(n\) integral with a deterministic midpoint scheme; it separately samples points on the orthogonal spherical lune, projects them gnomonically, computes the planar convex-hull vertex order, and sums spherical geodesic edge lengths. It also tests the derived uniform latitude bound at selected directions and calculates the beta-function coefficient. The executed standard-library run ended with `ALL_CHECKS_PASSED`.

The proof certificate is analytic rather than machine-certified: the claims that require mathematical reasoning are the Crofton normalization, the trivariate Gaussian orthant identity, the inverse-sine maximization at fixed latitude, and the dominated-convergence argument. Each is reconstructed explicitly in `RESULT.md`. Finite quadrature and Monte Carlo comparisons cannot certify an infinite-dimensional or infinite-sample limit. No separate expert or independent audit has been carried out.

The distribution is uniform in surface area on the unit two-sphere and the perimeter uses geodesic, not Euclidean chord, lengths. The result is an asymptotic equivalence for expected perimeter and does not assert a rate for the remainder beyond little-\(o\) relative to the leading deficit.
