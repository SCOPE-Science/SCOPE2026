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
# Verification record

The exact graph model is a 28/72/42-cell unordered cubical complex. With the adjoining `projection.json`, invoke `python3 verify.py` (Python 3 standard library). The executed checker returned:

`VERIFY_OK cells=28,72,42 H=(1,6,3) G=48 quotient_unit_minor=-1 torus_basis=3 extension_denominator=3 central_gluing_index=4`

The checker independently rebuilds edges, cells, signed boundaries, five stationary-particle loops and the junction exchange loop; proves connectedness and verifies the determinant-minus-one primitive quotient; and checks the three top-dimensional product tori and their unit minor. It calculates 48 first- and second-homology action matrices, checks all 2304 group-composition identities, verifies the determinant character, solves the equivariant section equations exactly in rational arithmetic, and verifies primitive antipodal eigenlattice bases with index four. The general topological interpretation uses the standard graph-configuration subdivision theorem; computations are exhaustive only for this specified finite graph. No separate independent external audit has been performed.
