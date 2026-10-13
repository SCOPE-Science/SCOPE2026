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

The infinite theorem is proved in `RESULT.md`. The bundled `verify.py` independently checks the finite algebraic lemmas and support classification.

It enumerates all \(242\) labeled posets through four points, forms their upset Heyting algebras, checks that complemented elements are unions of comparability components, and for every nonzero central element checks the maximal-point evaluation homomorphism and the graph-extension split. It also exhausts every nonempty Boolean-cell support through arity four and reconstructs a tuple realizing it.

Terminal output:

`VERIFY_OK 188184 exact assertions; 242 labeled posets through four points; 484 center/component checks; 468 center-splitting witnesses; 65809 nonempty truth-pattern supports through arity four`

The finite replay is not an infinite proof; atomlessness and density for the limit use universality and ultrahomogeneity. No independent audit has been performed.
