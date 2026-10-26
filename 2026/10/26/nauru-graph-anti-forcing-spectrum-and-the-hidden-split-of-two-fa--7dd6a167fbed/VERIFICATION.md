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

# Direct finite verification

From this folder run `python NAURU_VERIFY_EXHAUSTIVE.py`, then `python NAURU_VERIFY_CERTIFICATE.py NAURU_CERTIFICATE.json`.

The first checker independently enumerates all 120 matchings using uncovered-vertex recursion, and all edge-deletion subsets for each matching until the exact minimum is reached. The second checker uses a bipartite assignment to enumerate matchings, and checks the explicit eight-representative certificate: all image permutations preserve the entire edge set and cover every matching; each representative has a feasible deletion witness and as many alternating cycles with disjoint external edges as its claimed minimum; each minimum deletion-set count is checked by exhaustive subsets. Both programs use the standard library and assert all eight profile rows and the total 25,092.

The accompanying JSON outputs are execution records, not substitutes for the proof or for replay. The certificate has no dependencies on external graph software or an optimization solver. Publication-priority uncertainty, specialized unindexed sources, and the missing full text of a recent survey remain scientific limitations.
