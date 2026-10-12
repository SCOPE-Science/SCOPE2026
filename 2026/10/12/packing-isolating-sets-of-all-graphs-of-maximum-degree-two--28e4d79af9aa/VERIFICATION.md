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

Run `python3 artifacts/verify.py` with any standard Python 3 installation. The script has no external dependencies. It builds each path and cycle from its edge set and enumerates all vertex subsets. For each subset, it tests pairwise disjointness of closed neighborhoods and absence of an edge outside their union; the test does not use the gap classification. It independently computes the coefficient formulas and checks every coefficient. It then checks products for every unordered disjoint-union component profile of total order at most \(9\).

Actual replay output:

`ALL CHECKS PASSED; graphs_checked=221; vertex_subsets_examined=577328; connected_paths_and_cycles_n=1..17; all_multicomponent_profiles_total_order<=9`

No finite test certifies the statements for arbitrary \(n\); those are proved by the exact gap and cyclic-word arguments in `RESULT.md`. The status in front matter records the absence of independent external audit.
