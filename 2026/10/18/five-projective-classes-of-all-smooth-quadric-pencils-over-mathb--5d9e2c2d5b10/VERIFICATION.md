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

Run from this directory using Python 3 and no third-party packages:

```
python verify_census.py
python verify_base_smoothness.py
```

Expected terminal markers: `CENSUS_VERIFY_OK` and `BASE_SMOOTHNESS_VERIFY_OK`. The first implementation enumerates all 448 geometrically smooth quadratic forms using the exact six-bit Pfaffian test, constructs all 14,336 unordered binary two-spaces, checks 56 polar pencils each with 256 lifts, and closes orbits under adjacent variable swaps and a transvection. The second creates the two generators and all Jacobian two-minors on each of four affine charts, then runs Buchberger's algorithm for the base-smooth representatives; the unit ideal certifies geometric smoothness over the algebraic closure. Rational base points are directly evaluated at all 15 projective binary points. Smooth genus-one base existence for two orbits follows from the complete-intersection adjunction formula. The other three orbits are ruled out by the genus-one Hasse bound.

The output is a finite exact classification of the specified objects. It does not classify any unrestricted higher extension field, identify abstract curve isomorphism classes, or constitute an independent external audit.
