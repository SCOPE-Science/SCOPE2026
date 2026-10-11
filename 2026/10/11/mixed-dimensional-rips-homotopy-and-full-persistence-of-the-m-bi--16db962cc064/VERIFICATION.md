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

# Reproducible finite verification

`verify.py` and `morse_certificate.json` are the entire computational package. Run `python3 verify.py` in the same directory; Python 3 standard library suffices. The script reconstructs the graph from the displayed edge recipe, tests every BFS distance, verifies graph bipartiteness and unique distance-four pairs, and cross-checks all neighbor triangles and shared-edge multiplicities. It enumerates every simplex at each nontrivial filtration threshold by exhaustive 16-vertex masks.

Expected stdout:

```text
VERIFY_OK graph=GP(8,3) vertices=16 edges=24 distance4_pairs=8 f1=40 f2=248 f3=6560 morse_pairs=118 critical=(1,0,9,2) mod2_betti_scale2=(0,0,9,2)
```

The JSON certificate contains a chronological list of elementary free-pair deletions and maximal-cell critical deletions, each checked against the currently surviving entire face set. The script also independently computes exact binary boundary ranks. The structural graph-bipartition, acyclic matching and homotopy-pushout proof in RESULT.md, not extrapolation from finite data, establishes the integral homotopy classification. This verification does not claim any external or independent audit.
