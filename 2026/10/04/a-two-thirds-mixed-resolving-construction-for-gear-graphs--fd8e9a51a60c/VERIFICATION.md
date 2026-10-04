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

The checker constructs gear graphs from the edge definition, computes all-pairs vertex distances by breadth-first search, and computes edge distance as the minimum endpoint distance. It then tests mixed-signature injectivity directly.

```text
VERIFY_OK
construction_gears_checked = 57
distance_table_entries_checked = 110550
exhaustive_candidate_subsets_checked = 28507
exact_small_mixed_dimensions = [(4, 3, 8), (5, 4, 25), (6, 4, 3), (7, 5, 14), (8, 6, 56)]
G4_explicit_landmarks = (5, 6, 7)
G4_objects_resolved = 21
all constructions matched mdim upper bound ceil(2n/3)
published formula mdim(G_n)=n is contradicted for every tested n=4..60
```

The finite computations are corroborative. The infinite upper bound follows from the symbolic distance table and cyclic packing proof.
