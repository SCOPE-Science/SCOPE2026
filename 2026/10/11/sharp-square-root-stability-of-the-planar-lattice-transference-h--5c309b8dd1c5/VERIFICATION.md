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

# Reproducible finite checks and proof boundaries

Run `python verify.py` from the directory containing this file, using Python 3 and no extra packages. Observed output:

```
VERIFY_OK: 1500 exact rational blocking-hexagon tests; 201 certified square-root brackets; 13 lattice points enumerated
```

The script independently enumerates all integer points within the auxiliary polygon's complete bounded coordinate box; reconstructs a substantial deterministic family of perturbed admissible hexagons from six supporting lines; checks strict convexity, barycentric positivity, blocker collinearity, central symmetry, product identity and the three short lattice widths; and checks the claimed coordinatewise Hausdorff upper bound whenever the deficit lies within the theorem's range. A separate rational enclosure test verifies the square-root branch at 201 rational deformation parameters. Randomized-looking rational cases use a fixed seed and exact rational arithmetic throughout; no statistical confidence or infinite theorem follows from them.

The proof of the full continuum claim is analytic and is stated in RESULT.md: the determinant identity, multiplication under antipodal symmetry, the AM–GM product bound, inequality (2), exact factorization (3), Bernoulli estimate (4), barycentric estimates (5), and geometric support comparison (6). Its validity is not delegated to executable code. The earlier \(4/3\) universal inequality and equality case are background theorems, not independently recertified here. No external audit has taken place.
