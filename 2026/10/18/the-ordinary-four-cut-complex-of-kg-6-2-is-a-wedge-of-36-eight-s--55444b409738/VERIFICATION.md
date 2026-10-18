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

# Reproducibility and checked limits

Run the two self-contained Python 3 programs using only the standard library:

```
python3 verify_kg62_full.py
python3 check_original_kg62.py
```

The first program was executed against the actual package source and returned:

```
VERIFY_OK connected_4sets=750 disconnected_4sets=615 dual_nonempty_faces=1887 matched_pairs=925 critical_vertex=1 critical_4cells=36 hasse_covers=7455 DAG_nodes=1887 checked_7sets=6435 reduced_Euler=36
```

It enumerates every permitted face of the combinatorial Alexander dual, generates the specified deterministic matching, constructs every directed Hasse covering relation, proves acyclicity by visiting every directed node in a topological sort, and tests all seven-subsets. The second program was also executed against the actual package source and returned:

```
ORIGINAL_OK faces=30880 facets=615 full_7_skeleton=yes reduced_euler=36
```

This check independently builds the ordinary four-cut complex from disconnected four-sets and enumerates all its faces. Neither output by itself is the homotopy theorem: the proof additionally uses finite discrete Morse theory, combinatorial Alexander duality over the integers, connectivity from the full skeleton, Hurewicz, and the homological Whitehead theorem. The enumeration proves only the specified fifteen-vertex case, not an infinite Kneser-family statement. No assertion of external or independent audit is made.
