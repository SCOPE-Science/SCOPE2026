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

# Reproducible mathematical checks

Run `python3 verify.py` in a directory containing the embedded script, using the Python standard library only.

The verifier constructs the wheel edge set directly, enumerates all 4-cycles from vertex permutations, and enumerates all five-edge diamond subgraphs from choices of four vertices. In particular, it checks non-induced diamonds in the four-vertex clique. For every pair of graph edges it decides directly whether equality of their colors is forbidden by incidence or by the complete subgraph collection.

Observed completed results:

```
n=5 normalized=1 named=120
n=6 normalized=2 named=1440
n=7 normalized=367 named=1849680
n=8 normalized=11966 named=482469120
VERIFY_OK B/D direct graph conflicts, finite normalized census, transfer matrix, constructions
```

Tests include the complete 15-pair conflict graph for \(W_3\) under both variants; the 28-pair \(B\) and 26-pair \(D\) conflict graphs for \(W_4\); independent equality of \(B/D\) conflict sets for all rim lengths \(5\) through \(12\); exhaustive canonical rim assignments and matrix traces for rim lengths \(5\) through \(8\); constructive \(n\)-color wheel assignments for rim lengths \(5\) through \(15\); and the alternating two-new-rim-color construction for \(D(W_4)\).

The \(n\)-parameter theorem is established by the paper proof: finite computations cannot certify its unbounded quantifier. No independent external mathematical audit has been performed; the independent-audit evidence channel is unpopulated.
