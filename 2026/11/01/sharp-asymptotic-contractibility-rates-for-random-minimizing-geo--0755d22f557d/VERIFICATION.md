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

# Reproducibility

The complete analytic definitions, hypotheses, polygon coordinates, exact integral identities, Fourier limit argument, and equality proofs appear in RESULT.md. Run `python CHECK.py` with Python 3, SymPy, and NumPy available. The supplied checker was executed on the packaged source and printed:

```
SYMBOLIC_VORONOI_SECOND_MOMENTS_AND_SHARP_ENDPOINTS_PASSED
EXACT_RECTANGULAR_WINDING_BSPLINE_LAWS_PASSED
GLOBAL_SHAPE_OPTIMIZATION_CERTIFICATE_PASSED
INDEPENDENT_POLYGON_MOMENT_AND_DECK_CHECKS_PASSED
INDEPENDENT_RANDOM_GEODESIC_TRIANGLE_LIMIT_CASES_PASSED
INDEPENDENT_FOUR_AND_FIVE_VERTEX_WINDING_LAWS_PASSED
ALL_CHECKS_PASSED
```

The checker reconstructs the exact covariance from a six-vertex shoelace formula, proves the determinant identity symbolically, verifies sharp boundary cases and exact finite-sample rectangular spline values, and checks numerical geometry against independently generated interior-point samples and direct nearest-deck comparisons. Its randomized comparison is deterministic under the coded seed. Numerical checks do not establish the limiting theorem; the rigorous Fourier argument and sharp parameter optimization in RESULT.md do.

No independent review or external certification was performed. The asymptotic \(O_T(n^{-2})\) is not claimed uniform over degenerating lattice shapes. The finite-vertex global sharp inequality is not proved.
