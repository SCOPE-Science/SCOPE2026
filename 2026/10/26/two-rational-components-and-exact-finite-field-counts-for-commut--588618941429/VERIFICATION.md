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

The accompanying standalone Python 3 program `verify.py` uses only standard-library modules and directly implements the exterior wedge-product multiplication table.

Run: `python3 verify.py`

Expected terminal line: `VERIFY_OK_EXTERIOR_TUPLE_COMPONENTS_AND_COUNTS 1006 direct tests; t=3 component dimensions 160 171; t=10 496 535`.

The program exhaustively enumerates isotropic tuple conditions in canonical symplectic spaces of dimensions four and six over small fields, compares these exact counts against the isotropic-Grassmannian finite-field formula, checks 990 sampled tuples constructed from the independent affine parameters against *every* pairwise exterior-product equation over three odd fields, checks nondegeneracy of the degree-three pairing, and compares the length-two specialization against the previously established finite-field polynomial for four field orders. It also asserts the dimension transition and non-equidimensionality for selected lengths up to twenty.

Limits: none of these finite checks proves irreducibility, the formula for all tuple lengths, or the claims over arbitrary algebraically closed fields. Those follow from the explicit parametrizations, Lagrangian-incidence argument, and component separation in RESULT.md. The program does not test nonreduced scheme structure, characteristic two, or other exterior-generator counts.
