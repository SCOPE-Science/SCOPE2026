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

The proof uses only the shortest-path geometry of complete multipartite graphs. A selected pair in different parts has a length-one geodesic and covers no omitted internal vertex. A selected pair in one part has length two, and exactly one outside vertex can be chosen as the internal vertex of its fixed geodesic.

The checker independently represents each selected same-part pair as a one-use geodesic resource and computes a bipartite matching from omitted vertices to resources from different parts. It then tests minimality by deleting every selected vertex.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
strong geodeticity decided by explicit omitted-vertex/same-part-pair matching
all N and N-1 threshold classifications matched
all stated counts of maximum N-1 minimal sets matched
```

The exhaustive computation is finite corroboration only; the all-orders N and N-1 classification follows from the proof.
