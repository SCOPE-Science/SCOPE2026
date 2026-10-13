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

## Checks performed

An independent graph-distance computation was implemented in `verify.py`: for each edge and each vertex pair, it recomputes shortest-path distances after deleting that edge, assembles an edge-monitoring mask, and directly tests every selected subset in the finite test universe. The predicted leaf-and-gap criterion and the factorized polynomial were evaluated separately and agreed throughout.

The checker exhaustively covers all 3,898 labeled connected simple unicyclic graphs on three through six vertices and all 241,592 of their vertex subsets; it additionally checks 96 deterministic graphs on seven through twelve vertices, totaling 370,616 subset checks. The cyclic bounded-composition formulas were independently checked for all 16,376 cycle/attachment patterns with cycle lengths three through thirteen. Output is preserved in `verification_output.txt`; use `python3 verify.py` to reproduce it with the Python standard library.

## Boundaries

The finite tests do not verify all graph orders. The infinite statement follows from the proof's projection, short-gap equivalence, bridge-monitoring lemma, and exact composition bijections. Source comparisons and scientific limitations are documented in `REVIEW.md` and `AUDIT.json`; no independent external audit or validation has been performed.
