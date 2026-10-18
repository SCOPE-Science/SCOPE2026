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
# Finite verification

Run `python checker.py` with Python 3, without third-party dependencies. The packaged source is complete.

The checker exhaustively generated all agent equivalence-relation tuples for ten pairs of world and agent counts. It independently compared the maximum union-graph component diameter to the structural path-plus-color criterion, then compared exact extremer counts to the stated matrix recurrence. It enumerated 7,108 tuples in total.

For frames with at most four worlds and up to three agents, it tested the finite knowledge-unfolding truth-set semantics by direct iteration of modal preimages against breadth-first graph-radius neighborhoods: 234,098 truth-set steps passed. Direct nonempty disjoint-adjacent-subset word enumeration agreed with transfer counts for 18 parameter combinations, with two to four agents and lengths one to six.

Some exact extremal counts are: two agents and three, four, five worlds give 6, 24, 120; three agents and two, three, four worlds give 7, 36, 360; four agents and three worlds give 150.

Finite exhaustive testing is not an infinite proof, and a successful execution is not an independent mathematical audit. General quantifiers, the sharp lower-bound valuation, and the eigenvalue asymptotic are supported by the symbolic proof in `RESULT.md`.
