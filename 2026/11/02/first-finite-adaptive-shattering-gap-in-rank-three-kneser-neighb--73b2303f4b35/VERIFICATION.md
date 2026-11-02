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

`verify.py` is the reproducible Python 3 proof checker. It enumerates exactly all query/hypothesis triples for \(3\le n\le11\), proves the recurrence by exhaustive evaluation, checks both adjacent depths at each order, and validates each concrete leaf path of `trees.json`. The machine output is `output.txt`. The recursion pruning uses only rigorous cardinality bounds. This validates the finite adaptive theorem; it neither establishes an all-order formula nor separately re-proves the cited static VC values. No external audit was undertaken.
