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

The checker independently simulates the standard zero forcing rule for every vertex subset up through the minimum successful layer. It does not assume the omitted-pair classification.

For each complete multipartite type it then builds the token-jumping graph directly from symmetric differences of minimum sets and compares its full adjacency matrix with the line graph of the compressed complete multipartite graph.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
candidate_subsets_checked_through_minimum_layer = 63791
minimum_zero_forcing_sets_checked = 2502
admissible_pair_vertices_checked = 2448
orders = 2..10
all minimum-set classifications matched
all zero-forcing-graph adjacencies matched the claimed line graph
all order and diameter corollaries matched
```

The finite computation is corroborative only; the arbitrary-order theorem follows from the proof.
