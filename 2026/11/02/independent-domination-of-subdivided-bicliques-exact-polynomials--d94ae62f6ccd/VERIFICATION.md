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
# Direct definition-based checks

Run `python3 verify_inddom_subdivision.py` from the directory containing the script. No external Python packages or input files are needed.

The program constructs the full single-edge subdivision graph from original graph edges and enumerates nonempty vertex subsets, retaining those which satisfy both independent-set and domination conditions **directly**. Counts by cardinality are compared against the two claimed polynomial identities. It also verifies the claimed exact support and min/max coefficients on additional larger parameter pairs using integer arithmetic.

Executed result:

```
VERIFY_OK complete_bipartite_instances= 10 direct_bipartite_subsets= 715550 general_graph_instances= 31 direct_general_subsets= 1783 support_parameter_pairs= 136
```

The ten complete-bipartite instances comprise biclique parameters `(1,1),(1,2),(1,4),(1,6),(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)`. The 31 general examples are all labeled simple graphs on one, two, and three vertices plus 20 labeled four-vertex graphs. The 136 support checks use all parameters \(2\le a\le b\le17\). Exact integer arithmetic is used throughout.

These are finite consistency checks, not exhaustive certification of the infinite family. The general bijection and exact cardinality formulas are proved in `RESULT.md`; the asymptotic cites Ford's published Corollary 3 rather than attempting to verify it computationally.
