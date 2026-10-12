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

The checker constructs \(A_{r,t}\) directly, computes all-pairs shortest-path distances by breadth-first search, forms the sorted distance multiset from every vertex to every candidate landmark set, and compares representations on every edge.

It exhaustively enumerates all vertex subsets for fifteen parameter pairs: \(2\le r\le5\) at \(t=2,3,4\), and \(2\le r\le4\) at \(t=5\). It verifies every singleton basis in the star cases, every one-per-triangle basis in the friendship cases, and nonexistence of any local multiset resolving set in every checked larger-clique case.

Recorded output:

```text
VERIFY_OK
parameter_pairs_checked = 15
parameters = [(2, 2, 3), (3, 2, 4), (4, 2, 5), (5, 2, 6), (2, 3, 5), (3, 3, 7), (4, 3, 9), (5, 3, 11), (2, 4, 7), (3, 4, 10), (4, 4, 13), (5, 4, 16), (2, 5, 9), (3, 5, 13), (4, 5, 17)]
vertex_subsets_checked = 217496
finite_minimum_bases_checked = 78
t=2: local multiset dimension 1; every singleton is a basis
t=3: local multiset dimension r; bases choose one outer vertex per triangle
t>=4: no local multiset resolving set exists in every checked case
```

The finite enumeration is corroborative only. The all-parameter theorem follows from the exact representation formulas in the proof.
