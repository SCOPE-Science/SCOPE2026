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

# Verification of finite second De Morgan defect rigidity

The source `verify_second_demorgan.py` is standalone, standard-library Python 3 code. From the directory containing the files, execute:

```sh
python3 verify_second_demorgan.py
```

Checks performed: exhaustive enumeration of naturally labeled posets on one through six points (1, 2, 7, 40, 357, 4824); independent direct pseudocomplement and minimal-trace counting of ordered binary failures; direct unary weak-excluded-middle counts; the inequality between defects; the full equality classification; constructions attaining the cardinality bound for every algebra order 5–23; 200 higher-minimum ordinal-sum instances; and two eleven-element examples with identical unary but different binary defects. All checks use exact integers.

The expected terminal marker is:

```text
ALL_SECOND_DEMORGAN_CHECKS_PASS examined_posets=5231
```

The exhaustive range is finite; the stated universal claims rely on the proof in `RESULT.md`. The script does not establish historical originality and is not an independent mathematical audit.
