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

The standalone `verify.py` is Python standard-library-only. Run `python verify.py` in the directory containing that file. It forms the prescribed-consecutive-occurrence posets in two independent descriptions: adjacent rank relations with recursive deletion of minima, and complete pairwise rank relations with recursive deletion of maxima. For sixty parameter triples (overlaps 3 through 6, pattern lengths 2m+1 through 2m+3, copies 1 through 5), all exact counts match the predicted odd double factorials. It also checks the transitive-closure separator invariants and a cover relation.

Recorded execution: `VERIFY_OK cases= 60 overlap m=3..6 length K=2m+1..2m+3 copies j=1..5 two independent exact linear-extension counters and separator/cover checks sum_counts= 12828`.

These finite checks are not an exhaustive check of infinitely many parameters. The all-parameter correctness follows from the proof of the insertion recurrence in `RESULT.md`. The material has not undergone an independent audit, and historical completeness of the literature comparison is not certified.
