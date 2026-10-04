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

The checker independently reconstructs the complete multipartite graph from its part labels. It tests every nonempty vertex subset against the fort definition and checks inclusion minimality against every proper nonempty subset; it does not assume that deleting one vertex is sufficient for testing minimality.

The resulting minimal-fort hypergraph is compared exactly with the claimed pair-and-triple classification. Its matching number is computed by exact bitmask dynamic programming. Its fractional transversal number is computed from the fort-cover linear program using a linear-programming solver.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
nonempty_vertex_subsets_checked = 64788
orders = 2..10
minimal-fort classification matched exactly
size-2 and size-3 count formulas matched
fort-number matching formula matched
fractional zero-forcing LP formula matched
```

The finite computation is corroborative only; the arbitrary-order formulas follow from the proof.
