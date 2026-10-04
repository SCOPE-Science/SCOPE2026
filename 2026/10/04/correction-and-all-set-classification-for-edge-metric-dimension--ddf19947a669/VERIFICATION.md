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

The checker reconstructs graph distances rather than using the structural criterion as its decision rule. For each connected complete multipartite type of orders \(3\) through \(10\), it performs breadth-first search from every vertex, computes every vertex-to-edge distance, and enumerates every landmark set.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 127
vertex_subsets_checked = 64912
edge_instances_checked = 2925
orders = 3..10
all edge codes computed from BFS distances
all resolving-set classifications matched
all edge-metric dimensions and minimum-basis counts matched
K_{2,3,5}: published-size 7 construction fails; true dimension = 9
```

The explicit \(K_{2,3,5}\) test confirms that the published-size complement-of-one-per-part set is not edge resolving and that the true minimum size is \(9\). The finite computation is corroborative only; the arbitrary-order theorem follows from the proof.
