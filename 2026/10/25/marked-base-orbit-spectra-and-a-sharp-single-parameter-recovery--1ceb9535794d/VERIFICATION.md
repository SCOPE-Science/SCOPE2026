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

# Verification details

`verify.py` constructs the finite transformations of binary cross-edge states from the definitions of global complementation, left-side switches, right-side switches, both-side switches, and the unrestricted side-preserving group. It discards transformations changing any prescribed base cross-edge, then explicitly counts cosets of the remaining translation masks. With at most seven total vertices and ten free cross-edges, it compares 910 group/configuration instances against the closed rank formulas. On configurations with at most seven free edges it also enumerates the entire affine orbit partition rather than just group sizes.

The checker reproduces the singleton-base type counts in arities one, two, and three, balanced-side left/right agreement through arity seventeen, and the positive separation for unbalanced side sizes up to four using arity at most two. Its exact output is in `verify.out`.

The unrestricted statement is justified by the finite-group action argument and rank-nullity proof in `RESULT.md`. Finite tests neither prove infinite-arity correctness nor establish global originality. No external independent validation has been performed.
