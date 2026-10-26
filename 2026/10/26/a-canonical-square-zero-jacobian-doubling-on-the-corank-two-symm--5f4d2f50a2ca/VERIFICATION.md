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

The proof is self-contained in `RESULT.md`. Exact deterministic checks are supplied in `verify.py` (Python 3, standard library only). Running `python3 verify.py` outputs `VERIFY_OK` and complete rank-count distributions for every symmetric binary matrix of sizes 4 and 5. All computed gradients are evaluated **on the determinant hypersurface**: invertible alternating symmetric matrices may have all diagonal principal cofactors zero in characteristic two, without being singular points of that hypersurface.

The unbounded-size assertions follow from the exact Schur complement and adjugate arguments, not from enumeration. The transition identity for the nilpotent line is exact for every invertible kernel-frame matrix over characteristic two. The deeper corank-at-least-three Jacobian scheme is not classified. Independent auditing has not been performed.
