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

# Verification and limitations

The theorem is established by the self-contained proof in `RESULT.md`. The central-symmetry ratio and center are algebraic expressions for every integer \(m\ge1\) and every admissible apex ratio. No numerical experiment is required to establish their all-dimensional validity.

The standalone `verify_bicone.py` has no external dependencies. Run `python verify_bicone.py` in a directory containing the extracted files. The checker independently integrates the minimum of the two piecewise-affine section profiles in exact rational arithmetic, splitting at all breakpoints and crossings, and compares this with the displayed closed three-branch formula for 570 configurations. It also numerically integrates cubical-equator reflection overlaps for 25 dimension/height configurations with both axial and off-axis perturbations, and checks the explicit inverse at endpoints and interior values. The reproduced checker output is:

```
EXACT_RATIONAL_PIECEWISE_SLICE_INTEGRALS_PASSED 570
INDEPENDENT_CUBE_INTEGRAL_AND_SHIFT_CHECKS_PASSED 25
SHAPE_INVERSION_ENDPOINTS_AND_INTERIOR_PASSED
ALL_CHECKS_PASSED
```

The exact rational tests cover finitely many parameters; the numerical cubical integrations have floating-point error and do not certify the optimizer or the result for arbitrary bases. The analytic Brunn–Minkowski step, exact axial integrations and derivative signs supply the universal proof. The claimed unique center is compatible with the classical general uniqueness theorem of Stein, but its explicit coordinates are derived independently here. Historical novelty is not independently certified. An independent mathematical audit has not been performed.
