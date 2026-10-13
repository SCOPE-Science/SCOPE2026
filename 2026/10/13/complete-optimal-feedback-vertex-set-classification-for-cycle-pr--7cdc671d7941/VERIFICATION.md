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

The unlimited-order result is established by the column-cover, rung-contraction and cyclic-gap arguments in RESULT.md, not by computation alone. The included Python verifier performs independent disjoint-set cycle tests on labeled vertex subsets.

Command: `python3 verify.py` (standard library only).

Observed result:

```
VERIFY_OK orders=3..12 graph_combinations_checked=656077
columns: n,minimum_feedback_set_size,total_optimal,tree_complements,two_component_complements
3 2 6 6 0
4 3 32 24 8
5 3 20 20 0
6 4 132 96 36
7 4 56 56 0
8 5 448 320 128
9 5 144 144 0
10 6 1360 960 400
11 6 352 352 0
12 7 3840 2688 1152
```

For each order, the verifier checks all deletion subsets of the alleged optimum size and one less than that size. It compares direct forest recognition with an independently coded column-pattern prediction, including the component count. No finite verification is asserted beyond order \(12\). Literature priority and mathematical validity have not received independent audit.
