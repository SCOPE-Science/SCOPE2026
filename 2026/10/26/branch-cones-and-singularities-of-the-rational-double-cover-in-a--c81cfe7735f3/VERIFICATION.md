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

# Verification of the explicit double-cover classification

Run `python3 verify.py` from the package directory with Python and SymPy installed.

The checker asserts exact algebraic identities: the cubic substitution of the published parametrization, the inverse relations generating the source function field, the nontrivial involution, the two cone equations, the triple-line scheme equation, and the derivative structure. It also verifies squarefreeness of the degree-four branch-form tangent cone and the structure of the degree-three contact slice. These checks are symbolic rather than numerical approximations.

The proof of normality and generic transverse analytic classification uses regularity, the implicit-function theorem and unit removal, not a finite sample. The canonical formula uses standard double-cover adjunction. Independent audit has not been performed; no external certification is asserted.
