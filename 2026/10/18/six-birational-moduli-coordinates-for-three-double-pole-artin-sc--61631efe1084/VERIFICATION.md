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

The packaged standalone `verify.py` was run with Python 3 and SymPy. It checked exact Möbius-coordinate equalities for both generating transpositions, all six displayed invariants under every one of the twelve group elements, and three Cramer's-rule determinant identities. It also computed the symbolic Jacobian determinant and proved it is a nonzero polynomial modulo characteristic three.

Expected output:

`VERIFY_OK marked_poles=3 symmetries=12 invariants=6 generic_jacobian_nonzero=True`

`jacobian_det_factorization= 2*(A0 - A1)**3*(A0 - A2)**3*(A1 - A2)**3*(A0 + A1 + A2)**3`

The formal proof additionally requires the genus-seven ramification calculation, uniqueness of the degree-three pencil, and invariant-field reconstruction. The script does not certify historical novelty, full invariant-ring generation, or behavior outside the dense open set.
