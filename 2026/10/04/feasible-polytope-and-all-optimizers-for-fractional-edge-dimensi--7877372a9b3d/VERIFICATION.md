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

The checker rebuilds every complete multipartite graph from its part labels, computes all-pairs distances by breadth-first search, and constructs every edge resolving neighborhood from the definition. It then solves the original vertex-level LP and, subject to the optimum objective, independently minimizes and maximizes every coordinate.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 127
edge_pairs_checked = 39961
coordinate_optimization_LPs = 2098
orders = 3..10
all exact reduced-constraint generators matched
all original vertex-level LP optima matched
all optimizer coordinate ranges matched
```

The finite computation is corroborative only; the arbitrary-order theorem follows from the proof.
