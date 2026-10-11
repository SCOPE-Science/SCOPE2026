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

Run `python3 verify.py`. It imports only Python 3 standard-library modules and constructs complete Hamming shells using combinations. For each of 35 shells in dimensions 5 through 11, it applies the **actual** degree-two Walsh Gram matrix to three explicit test functions (constant, one-point difference, and a product of two disjoint point differences), verifies their eigen-equations and the full trace against the claimed multiplicities, and independently checks the collision criteria. It then evaluates the closed rational spectrum for 123,752 dimension-radius pairs with dimensions up to 500, checking all exceptional equalities using integer arithmetic. The verified output is:

```
VERIFY_OK eigenpair_cases=35 arithmetic_collision_cases=123752
```

The checker verifies finite examples; the full infinite claim, positive spectral multiplicities, and the exact Diophantine collision characterization follow from the complete algebraic derivation in `RESULT.md`. Matrix sizes above the enumerated range and higher Walsh degree are not certified by enumeration or asserted in the theorem. Independent external audit has not been performed.
