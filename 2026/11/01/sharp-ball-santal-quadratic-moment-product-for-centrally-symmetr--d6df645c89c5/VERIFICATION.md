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

# Verification of the quadratic polar-moment certificate

The file `verify.py` can be executed with Python 3 and SymPy. It rebuilds both polygons from normalized zonotope generators, computes the polar by intersecting consecutive supporting lines, and integrates the exact quadratic moments by polygon formulas. It checks the symmetric rational profile, the 46 coefficients in the ordered-gap upper-deficit polynomial, equality rigidity, the 19 positive lower-deficit coefficients, two endpoint values and 20 separate rational parameter instances. Successful replay reports the exact affine-regular value of \(25/24\).

The inequalities for all admissible parameters follow from positive-coefficient identities given in `RESULT.md`; the 20 parameter instances are examples rather than an exhaustive search. The outcome does not constitute external or independent validation, and priority among older publications is not established by a finite literature search.
