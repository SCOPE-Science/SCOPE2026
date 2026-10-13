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

The checker constructs the half graph \(H_n\) for
\[
2\le n\le9.
\]

It computes all-pairs shortest-path distances and the edge-distance vector from every candidate landmark set to every graph edge. It separately checks the vertex-cover condition.

All subsets of size \(n-1\) are tested and fail to cover the diagonal matching. Every subset of size \(n\) is then tested. The checker compares both the complete set of minimum vertex covers and the complete set of dominant edge metric bases with
\[
C_t=\{a_1,\ldots,a_t\}\cup\{b_{t+1},\ldots,b_n\},
\qquad0\le t\le n.
\]

Recorded output:

```text
VERIFY_OK
n=2: Ddim_e=2, minimum_vertex_covers=3, dominant_edge_metric_bases=3
n=3: Ddim_e=3, minimum_vertex_covers=4, dominant_edge_metric_bases=4
n=4: Ddim_e=4, minimum_vertex_covers=5, dominant_edge_metric_bases=5
n=5: Ddim_e=5, minimum_vertex_covers=6, dominant_edge_metric_bases=6
n=6: Ddim_e=6, minimum_vertex_covers=7, dominant_edge_metric_bases=7
n=7: Ddim_e=7, minimum_vertex_covers=8, dominant_edge_metric_bases=8
n=8: Ddim_e=8, minimum_vertex_covers=9, dominant_edge_metric_bases=9
n=9: Ddim_e=9, minimum_vertex_covers=10, dominant_edge_metric_bases=10
candidate_subsets_checked = 125472
all size-n minimum vertex covers were exactly the n+1 canonical cuts
every canonical cut edge-resolved the half graph
```

The finite computation is corroborative only. The theorem for every \(n\ge2\) follows from the matching lower bound, the classification of maximum independent sets, and the explicit threshold form of the edge-distance vectors.
