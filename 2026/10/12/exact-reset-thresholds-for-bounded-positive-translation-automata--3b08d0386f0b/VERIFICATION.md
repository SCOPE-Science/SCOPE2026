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

# Reproducibility

Run `python3 verify.py`. The standalone Python program uses a subset-automaton breadth-first search without external dependencies to obtain exact shortest reset lengths for every tested pair, and separately replays the constructive word. It prints `VERIFY_OK` on success. The proof in RESULT.md establishes all infinitely many integer parameter pairs; finite checks are not used as an infinite certificate.

Observed reproducibility output:

```text
VERIFY_OK 105 exact independent subset-automaton BFS instances, n=2..16 m=1..7; constructed reset words replayed
```

Scientific scope: positive directed jumps, no wraparound, failed jumps remain fixed. No independent audit has been performed.
