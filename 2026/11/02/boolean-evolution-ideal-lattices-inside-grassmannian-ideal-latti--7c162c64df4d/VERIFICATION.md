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

The proof identifies all nonzero ideals by propagation of squared generators along a connected base graph, and all extendible natural bases by orthogonality of their fibre projections. It then uses the exact adjacency spectrum of an independent-fibre blowup and standard regular-graph Cheeger inequalities to prove expansion preservation.

A Python 3 standard-library program, `verify.py`, was executed in the same package directory and printed `VERIFY_OK`. It exhaustively enumerated all linear subspaces and tested the ideal condition for the blowups of `K2` over fields of orders 2 and 3 and `K3` over the field of order 2. It independently enumerated the projective natural-basis candidates in dimension four over the field of order 3 and found five ideals with an extendible natural basis, compared with seven ordinary ideals. It checked orthogonal bases over the rational numbers and all graph cuts in four small examples. The printed trace is not a substitute for the all-dimensional proof.

The real-field statement about positive-definite fibre forms does not extend unchanged to arbitrary coefficient fields. Full historical priority and independent mathematical certification have not been established.
