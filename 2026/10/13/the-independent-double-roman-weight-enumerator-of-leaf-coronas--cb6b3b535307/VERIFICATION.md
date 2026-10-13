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
# Verification of the complete corona enumerator

The included standalone Python 3 script `verify_idrd_corona.py` has no external dependencies. For every base graph tested it enumerates all \(4^{2n}\) independent double Roman *candidate* labelings, checks all Roman-defense and positive-support-independence conditions on the actual corona adjacency, and constructs a separate predicted polynomial directly from independent subsets \(I\subseteq V(G)\) and their open-neighborhood cardinalities.

The script checks every labeled simple base graph on \(1\), \(2\), \(3\), or \(4\) vertices (respectively \(1\), \(2\), \(8\), and \(64\) choices), plus four five-vertex graphs: the path, cycle, star, and complete graph. Thus it checks \(79\) base graphs and \(8{,}421{,}904\) labelings. All coefficients, not merely the minima, agree with the proposed transform; the independent-domination minimum is also independently computed and checked.

Actual verifier output:

```text
ALL_LABELINGS_OK_n=1_graph_count=1
ALL_LABELINGS_OK_n=2_graph_count=2
ALL_LABELINGS_OK_n=3_graph_count=8
ALL_LABELINGS_OK_n=4_graph_count=64
P5: all_functions=57, min_count=3, i(G)=2
C5: all_functions=61, min_count=5, i(G)=2
K1,4: all_functions=47, min_count=1, i(G)=1
K5: all_functions=81, min_count=5, i(G)=1
P4: gamma=10, min_count=5, indep_dom=2
graphs_checked= 79
labelings_checked= 8421904
VERIFY_OK
```

The arbitrary-order result is proved by the exact bijection, not by extrapolation from these finite computations. Only graphs with one leaf per core vertex are covered by the mathematical result.
