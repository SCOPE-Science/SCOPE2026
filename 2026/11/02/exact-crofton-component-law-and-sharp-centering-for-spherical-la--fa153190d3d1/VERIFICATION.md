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
# Reproducibility and evidential limits

Run `python3 spherical_zone_components_check.py` in a directory containing the embedded checker. The checker uses only the standard library and evaluates the component count directly from random-plane geometry rather than evaluating the same derived trigonometric integral. Its observed success markers are:

```
INDEPENDENT_KINEMATIC_MIDPOINT_INTEGRALS_PASSED 9 x 313600
INDEPENDENT_RAW_HAAR_AFFINE_PLANE_SIMULATIONS_PASSED 4 x 170000
RIGID_AREA_FRACTION_IDENTITY_AND_SHARP_SHAPE_ORDER_PASSED
FIXED_AREA_STRICT_SHAPE_ORDER_AND_HALF_AREA_THRESHOLD_DIAGNOSTICS_PASSED
SHARP_ONE_SIDED_SQUARE_ROOT_ONSET_DIAGNOSTICS_PASSED
ALL_CHECKS_PASSED
```

The mathematical proof is in RESULT.md. Numerical comparisons and finite grids are diagnostic only. No independent mathematical audit has been performed. The probability model and its boundaries must be preserved when applying the formulas.
