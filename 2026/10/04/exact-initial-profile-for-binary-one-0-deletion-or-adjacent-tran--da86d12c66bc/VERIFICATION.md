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

`verify.py` reconstructs every error ball for every binary word at lengths \(1\) through \(7\) using two separate implementations and requires exact agreement. It then builds the compatibility graph in which an edge means disjoint error balls.

The explicit codes in `artifacts/optimal_codes.json` are checked to be valid and to have sizes matching `artifacts/profile.csv`. Exact maximum-clique branch-and-bound then proves that no larger code exists. Its pruning bound is a greedy coloring of the current candidate graph: every clique contains at most one vertex of each color, so the color count is an upper bound on any extension.

The packaged replay ends with `VERIFY_OK profile=2,3,4,7,11,17,30`. The claim is limited to these seven finite lengths; no computation beyond this range is used as evidence.
