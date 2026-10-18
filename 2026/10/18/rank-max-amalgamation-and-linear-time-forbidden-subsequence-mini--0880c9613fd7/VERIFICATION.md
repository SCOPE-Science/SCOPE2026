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

The proof consists of the monotonic lower bound, the greedy pattern-phase amalgamation, and the rightmost-embedding deletion invariant. The phase construction applies to any finite number of inputs; the reduction is self-contained for any number. All pattern and input boundary cases described in RESULT.md are explicit.

`checker.py` and `tests_output.txt` are included as replayable finite checks. The script uses the standard library, exhaustive binary testing, a separate deletion-based minimality reference, seeded randomized quaternary testing, and a growing-gap family. These finite results do not establish the universal claim by induction or certification; mathematical reasoning is required. The scientific literature comparison does not rule out every unindexed publication. No independent audit or external validation was performed.
