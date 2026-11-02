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

## Direct checks

Run the standalone Python 3 standard-library program `python verify_hyperbolic_acuteness.py` from the same directory as this document. The program checks the one-dimensional exact gap integral independently against an absolutely convergent odd dilogarithm series at five positive radii. It also constructs the Poincaré geodesic as a Euclidean circle orthogonal to the unit-disk boundary, computes the two initial geodesic tangent vectors at each vertex, and compares the resulting direct acuteness frequency with the theorem at four radii using 25,000 independently sampled triangles per radius.

The actual completed run printed:

```
INDEPENDENT_GAP_INTEGRALS_AND_ODD_DILOG_SERIES_PASSED 5
DIRECT_POINCARE_GEODESIC_TANGENT_MONTE_CARLO_PASSED 0.3 25000
DIRECT_POINCARE_GEODESIC_TANGENT_MONTE_CARLO_PASSED 1.0 25000
DIRECT_POINCARE_GEODESIC_TANGENT_MONTE_CARLO_PASSED 2.0 25000
DIRECT_POINCARE_GEODESIC_TANGENT_MONTE_CARLO_PASSED 3.0 25000
SMALL_RADIUS_COEFFICIENT_DIAGNOSTICS_PASSED
ALL_CHECKS_PASSED
```

## Limits of checking

The quadrature is finite, the series is truncated after an explicit large number of terms, and the simulations are finite and random. They do **not** prove any statement for the continuum of all radii; this requires the analytic trigonometric factorization, exact change-of-variables Jacobian, integral differentiation, and derivative and endpoint arguments in `RESULT.md`. Historical novelty is provisional and independently validated publication priority has not been established.
