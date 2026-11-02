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

Run `python3 verification/checker.py` using Python 3.9 or later (standard library only). The executable checks the high-precision stationary-point value against the formula, the hemisphere and collapsed-lune endpoints, the monotone profile on a diagnostic grid, and independent two-point Monte Carlo sampling on four spherical lunes using a fixed pseudorandom seed.

The executed checker returned:

```text
STATIONARY_POINT_AND_EXACT_HEMISPHERE_LIMIT_PASSED
DIRECT_PROFILE_GRID_DIAGNOSTIC_PASSED 513
INDEPENDENT_AREA_UNIFORM_TWO_POINT_SIMULATIONS_PASSED 4
ALL_CHECKS_PASSED
```

The proof's globally strict monotonicity of \((\tan t-t)/t^3\), and hence uniqueness of the minimizer, follows from explicit differentiation in `RESULT.md`; the 513-point grid does **not** certify it. The numerical root is an approximation; its exact definition is the unique root in the stated interval.
