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

The theorem follows from the symbolic counting proof in RESULT.md. Finite tests below are an independent falsification attempt, not an all-size proof.

Run `python3 verify_popularity.py` with Python 3. The standard-library-only program checks exact agent vote margins with two independent approaches: explicit labeled partitions for all populations with one, two or three triple rooms, and integer Hungarian assignments of initial versus new occupant categories for all allowed composition profiles in specified finite ranges. Output observed:

```text
SPARSE_GENERAL_CHECK_OK 403 composition profiles with room size 2..7 and rooms 1..6
TRIPLES_COMPOSITION_CHECK_OK 329 profiles; 1843 comparisons; 238 noncanonical profiles
Exact popular counts: [(2, 3, 9), (3, 3, 90), (3, 4, 180), (4, 6, 8100)]
DIRECT_LABELED_ENUMERATION_OK 21 profiles; room counts 1..3
```

All tests terminate normally and match the symbolic classification. Direct enumeration covers complete partitions only at the stated small sizes; large-size validity rests on the proof. No probabilistic, heuristic, or external database computation is needed to establish the theorem.
