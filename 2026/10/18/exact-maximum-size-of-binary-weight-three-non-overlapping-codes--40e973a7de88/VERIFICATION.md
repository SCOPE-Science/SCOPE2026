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

The all-length correctness argument is the rotation-orbit upper bound and an explicit construction with matching cardinality, provided in `RESULT.md`. A separate exhaustive checker in `check.py` checks all codewords, all ordered nonempty proper suffix–prefix comparisons, and exact coverage of the primitive weight-three rotation classes for lengths 3–30. Running `python3 check.py` completes without assertions.

The finite calculation does not establish any assertion beyond its enumerated range. The symbolic proof supplies the infinite-parameter statement. Originality was compared against identified literature and searchable research claims, with the usual residual risk of unindexed or differently named prior results. No independent mathematical audit or formal proof assistant check has been performed.
