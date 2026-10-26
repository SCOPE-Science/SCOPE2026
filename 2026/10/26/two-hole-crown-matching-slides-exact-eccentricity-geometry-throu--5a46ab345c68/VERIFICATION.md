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

The two included standard-library Python checkers independently enumerate all crown matchings of size \(n-1\) for \(3\le n\le8\), using derangement swaps versus direct partial-injection slides. Both executed successfully, and their complete canonical JSONL outputs agree byte-for-byte. Every BFS visits all states and every local edge is checked for reciprocity. The finite diameter and eccentricity classification follows from one full BFS per orbit of simultaneous index relabelings, whose orbit formula is proved in RESULT.md.

Run `python3 verify_permutations.py` and `python3 verify_matchings.py` and compare stdout to `permutation_output.jsonl` and `matchings_output.jsonl`. These calculations do not verify any all-order distance claim; the all-order bijection, degree and parity identities are separately proved. The previously published connected-claw-free reachability theorem is credited, not re-proved as a new theorem. All literature comparisons and publication-priority caveats are documented in REVIEW.md and AUDIT.json.
