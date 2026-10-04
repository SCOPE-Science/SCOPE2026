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

The checker constructs each broom from an adjacency list, computes all-pairs shortest-path distances, enumerates every vertex subset, and tests the outer multiset resolving condition directly by sorting the distances from every outside vertex to the chosen set.

For every tested parameter pair it then compares the true minimum sets with the theorem's complete list: the full brush, or exactly one omitted brush leaf replaced by one non-root handle vertex.

Recorded output:

```text
VERIFY_OK
broom_parameter_pairs_checked = 35
vertex_subsets_checked = 251968
minimum_bases_checked = 910
parameters brush = 3..7, handle = 2..8
all outer multiset dimensions equal the brush size
all minimum bases match the complete classification
all basis counts equal 1 + brush*handle
```

The finite computation is corroborative only. The theorem for every \(q\ge3\) and \(\ell\ge2\) follows from the proof.
