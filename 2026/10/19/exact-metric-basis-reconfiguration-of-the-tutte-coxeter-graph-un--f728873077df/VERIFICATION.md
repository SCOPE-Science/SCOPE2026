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

# Computational verification

The complete source files `verify_metric_A.py` and `verify_metric_B.py` are included alongside their captured outputs `verify_metric_A.out` and `verify_metric_B.out`. Both run with a standard Python 3 interpreter without dependencies or external data. Execute:

```
python3 verify_metric_A.py
python3 verify_metric_B.py
```

The first script builds the duad–syntheme incidence graph, tests all \(\binom{30}{k}\) subsets for \(1\le k\le6\) by exact pair-separation sets, lists every six-vertex metric basis, and constructs the complete one-token-jump graph and its incidence-restricted slide subgraph. It verifies the adjacent-transposition generators of \(S_6\) directly on all graph edges, exhausts their 62 basis orbits, and performs full breadth-first search from a representative of each orbit.

The second script builds the incidence graph from the symplectic space \(\mathbb F_2^4\), uses direct distance-signature uniqueness rather than separation masks, builds jumps by shared-five-element buckets, slides by direct neighbor substitution, and validates symplectic transvections and 62 complete orbits before performing all 62 searches. Both paths assert the figures published in the finding and produce terminating success markers. Their checked graph is finite, so these exhaustive loops establish all claimed finite quantifiers; the scripts do **not** support generalizations beyond this graph.

The two checks were performed together as a self-review. The presence of separate algorithms is not equivalent to external independent validation or audit, which has not been performed. The previously known metric dimension is acknowledged, and the absence of a complete contemporary thesis inspection remains an originality limitation.
