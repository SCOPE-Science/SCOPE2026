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

The standalone checker implements the definitions directly from adjacency, without using the proof classification.

For the five-vertex graph it exhausts all \(3^5\) labelings, verifies
\[
\gamma_I^s(G)=3,
\]
and verifies that the unique minimum labeling on \((\ell,x,y,p,q)\) is
\[
(0,2,1,0,0).
\]
It also checks that transferring one unit from \(x\) to \(\ell\) gives \((1,1,1,0,0)\), which is Italian dominating but not secure Italian dominating.

For smallest-order verification, the program enumerates every labeled simple graph on one through four vertices, retains every graph with at least one degree-one vertex, computes all minimum SIDFs, and verifies that each such graph has a minimum function assigning label \(1\) to every leaf.

Recorded output:

```text
VERIFY_OK
target_order = 5
target_edges = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
target_gamma_secure_italian = 3
target_minimum_functions = 1
target_unique_minimum = (0, 2, 1, 0, 0)
transferred_leaf_function_is_italian = True
transferred_leaf_function_is_secure = False
smaller_leaf_graphs_by_order = [(1, 0), (2, 1), (3, 6), (4, 49)]
smaller_leaf_graphs_checked = 56
smaller_graph_labelings_checked = 4140
smaller_counterexamples = 0
```

The finite enumeration proves smallest order because it is exhaustive over all simple graphs of lower order, not a sample. The five-vertex correctness and uniqueness claim also has an independent symbolic proof in RESULT.md.
