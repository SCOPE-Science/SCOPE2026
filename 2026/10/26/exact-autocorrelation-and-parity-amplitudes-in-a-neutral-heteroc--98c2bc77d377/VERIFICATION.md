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
# Verification

`check.py` is a standalone Python 3 standard-library program. It independently constructs the walk path weights, expands the Catalan first-passage formal power series, and integrates the actual piecewise-affine map over rational dyadic rectangles. It checks matching correlation coefficients at orders zero through twelve for walk versus series and zero through six for planar map versus series. It also asserts seven explicit low-order rational values. All checks pass using exact arithmetic.

These are finite independent computational consequences, not an infinite proof. The infinite generating function follows by the path-minimum and first-hitting-time decomposition, and the parity constants by two branch-point singularity expansions, both written explicitly in `RESULT.md`. The implementation uses no downloaded data and no external computational dependencies.

Mathematical priority of an exact equivalent statement outside examined literature remains open to further independent investigation. No external audit has been conducted.
