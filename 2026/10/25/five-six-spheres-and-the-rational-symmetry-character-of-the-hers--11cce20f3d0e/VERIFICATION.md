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

Run `python3 verify.py` in this directory with Python 3 (standard library only). The script recomputes all facets and the entire face set, constructs the exact face-poset matching, and confirms acyclicity on the complete reversed Hasse diagram, not merely by checking isolated gradient paths. It verifies all twelve signed Lefschetz traces and the rational representation character.

Recorded direct execution:

```text
VERIFY_OK
oriented_spanning_paths 444
undirected_spanning_paths 222
nonempty_faces 37454
f_vector [18, 153, 796, 2742, 6402, 9913, 9738, 5694, 1776, 222]
morse_pairs 18724
critical_cells {0: 1, 6: 5}
nonempty_hasse_incidences 237072
acyclic_vertices_toposorted 37454
S3_times_C2_character_classes id=5,transposition=-1,threecycle=-1,central=1,central_transposition=-1,central_threecycle=1
full_group_invariant_dimension 0
```

The proof of the homotopy type uses the acyclic discrete-Morse theorem after complete finite enumeration. Rational symmetry is computed from signed fixed-face traces, with no assumption that an arbitrary Morse matching is equivariant. Exact integer arithmetic is used throughout. No independent audit has been performed; computational replication is not a claim of independent mathematical validation.
