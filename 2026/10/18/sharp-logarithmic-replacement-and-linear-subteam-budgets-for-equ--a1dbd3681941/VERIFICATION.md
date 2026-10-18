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

# Reproduction and limits

Run `python3 verify_team_bounds.py` with a standard Python 3 installation (only `itertools` is used). The script exhausts all nonempty subsets of the entire assignment space for the listed alphabet/arity combinations, verifies replacement minimums per complete equality–constancy profile, computes exact minimum preserving subteams by finite dynamic programming, and checks its independent greedy partition-refinement implementation. It also checks staircase sharpness on several other sizes. The printed terminal marker must be `SHARP_SMALL_TEAM_BOUNDS_VERIFY_OK`.

The mathematical proof in `RESULT.md` establishes the theorem for every finite alphabet and arity; finite checks cannot certify those infinite families. The semantic transfer relies on the published equality–constancy invariance lemma. Historical priority beyond the sources described in `REVIEW.md` is not independently certified.
