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

# Reproducibility and finite checks

The embedded `verify.py` requires only Python 3 standard library. Execute `python3 verify.py` next to these files. It implements the deleted-matching adjacency directly, tests every subset at each order \(3\le n\le8\), enumerates all feasible add–delete edges, and computes actual connected components by graph traversal. It verifies all 33 pairs \((n,k)\) with \(2\le k\le n+1\), checks the star decomposition at \(k=3\), the count of isolated minima at \(k=4\), and the two extra entire-side isolates at \(k=n\ge5\).

The observed run printed:

`VERIFY_OK orders=3..8 cases=33 set_visits=165129 edge_visits=954140 component_counts={3: {2: 3, 3: 5, 4: 1}, 4: {2: 4, 3: 4, 4: 9, 5: 1}, 5: {2: 5, 3: 5, 4: 31, 5: 3, 6: 1}, 6: {2: 6, 3: 6, 4: 91, 5: 1, 6: 3, 7: 1}, 7: {2: 7, 3: 7, 4: 211, 5: 1, 6: 1, 7: 3, 8: 1}, 8: {2: 8, 3: 8, 4: 421, 5: 1, 6: 1, 7: 1, 8: 3, 9: 1}}`

These are finite computations, not a proof for all orders. The symbolic argument in `RESULT.md` covers arbitrary admissible integers. This package has self-review only; independent audit is not performed.
