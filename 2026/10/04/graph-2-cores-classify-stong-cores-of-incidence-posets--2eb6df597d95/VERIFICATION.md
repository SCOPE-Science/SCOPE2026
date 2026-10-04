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

The theorem is proved symbolically in `RESULT.md`. The executable check is a finite regression, not a substitute for the infinite proof.

`verify.py` enumerates every labeled finite simple graph on one through six vertices. For each graph it independently computes the graph-theoretic 2-core and the number of tree components. It then performs the proposed paired incidence-poset reductions: a degree-one graph vertex must be an up beat point; after its deletion, the incident edge must be a down beat point. At termination it checks the predicted core cardinality, verifies that the non-isolated surviving incidence elements are exactly those of the graph 2-core, checks that the number of isolated survivors equals the number of tree components, and confirms that the result has no beat points.

The exact replay output bundled in `verification_output.txt` is:

```
VERIFY_OK
labeled_graphs_checked 33867
graphs_by_order [(1, 1), (2, 2), (3, 8), (4, 64), (5, 1024), (6, 32768)]
beat_deletions_replayed 78152
max_beat_deletions_single_graph 10
cycle_core_sizes {3: 6, 4: 8}
```

The explicit triangle and square checks illustrate a boundary: both underlying graphs have ordinary homotopy type \(S^1\), but their incidence-poset Stong cores have different cardinalities and hence are not homotopy equivalent as finite spaces.

Limits: exhaustive enumeration stops at six graph vertices; no finite enumeration is claimed to certify the all-graph theorem. The symbolic argument establishes the quantified result.
