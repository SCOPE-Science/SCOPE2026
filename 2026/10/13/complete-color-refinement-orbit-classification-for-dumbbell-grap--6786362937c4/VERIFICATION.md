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

The general classification is established by the proof in RESULT.md. The separate finite replay dumbbell_replay.py constructs each graph, performs uniform color refinement, and compares the stable partition with the automorphism-orbit description justified by the graph structure. It also records the first attachment split round.

The executed replay covered 3<=p,q<=18 and 0<=k<=50 and returned:

```json
{"orbit_checks":13056,"split_checks":12240,"balanced_partition_checks":16}
```

Replay: `python3 dumbbell_replay.py`. SHA-256: `4ed0c74cefa51ab00d8eefef439b43c1660e0a7890d2d64c8222afc655c976f6`.

This finite check does not establish originality, value, or the all-parameter theorem. Independent audit has not been performed.
