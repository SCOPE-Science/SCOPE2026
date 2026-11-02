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

# Verification evidence and limitations

The embedded `checker.py` explicitly implements the positive box and diamond membership predicates over all upsets of finite chains. Running `python checker.py` visits every local neighbourhood family on carriers with one through six worlds, compares actual truth tables of nullary and unary operations against the proposed `(empty-flag, min/max-nonempty)` profiles, checks the count and size of each class, and directly checks binary-instance reductions on carriers through four worlds. Successful replay concludes with `ALL_CHECKS_OK`. The displayed values are 4, 6, 8, 10, 12, 14 distinct local signatures per modality and largest fibers 1, 2, 4, 8, 16, 32 for carriers of size one through six.

The general arity and fiber claims are proven in RESULT.md from total ordering of upsets; the finite checker is an independent implementation of the semantic clauses, not a proof for unbounded carrier size. The homogeneous product count is algebraic, not brute-force enumeration of every pair at size six. A historically exhaustive literature-priority determination is not claimed. No independent external audit has been performed.
