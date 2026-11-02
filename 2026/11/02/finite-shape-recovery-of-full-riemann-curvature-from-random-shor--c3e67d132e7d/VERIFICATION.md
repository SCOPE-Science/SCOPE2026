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

# Reproducibility and limits

The algebraic curvature observation map and its rank-one/rank-two inverses were checked exactly for dimensions 2 and 3 by `check_curvature.py`. `check_rank.py` checks full column rank over the prime field of order 104729 in dimensions 2, 3, 4, 5; the respective ranks are 1, 6, 20, 50, and the algebraic genericity argument independently establishes the all-dimensional statement. `check_spaceform.py` samples exact spherical distance and integrates the exponential-map volume Jacobian for an anisotropic two-dimensional tangent ellipsoid, cross-checking the limiting formula at three radii. Its finite-radius errors and Monte Carlo/quasi-Monte Carlo tolerances are not proof of the asymptotic expansion.

The proof itself depends on the standard normal-coordinate squared-distance expansion, the volume Jacobian expansion, moment contractions and the algebraic curvature symmetries; it does not depend on external verification services, unpublished papers or numerical extrapolation. No independent mathematical audit has been performed.
