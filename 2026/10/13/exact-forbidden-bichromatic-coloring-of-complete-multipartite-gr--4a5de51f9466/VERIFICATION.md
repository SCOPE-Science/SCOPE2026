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

The proof is structural and does not depend on finite computation. A standalone checker nevertheless performs an exhaustive finite stress test of the formula.

For every nondecreasing host part-size vector with \(2\le r\le4\) and \(1\le n_i\le5\), the checker enumerates every integer partition of each \(n_i\). Each integer partition represents all possible color-class-size multisets inside that host part, which is sufficient because the forbidden-copy condition depends only on class sizes. It then tests every combination of such multisets against every pair \(1\le s\le t\le4\) with \(t\ge2\), computes the true minimum number of classes, and compares it with the closed formula.

Expected successful output:

`ALL CHECKS PASSED; parameter_cases=1080; host_parts=2..4; part_sizes=1..5; shore_sizes=1<=s<=t<=4,t>=2`

This finite enumeration checks only the stated bounded ranges and is not an exhaustive proof for unbounded parameters. The infinite claim rests on the complete-bipartite embedding criterion and the two-regime argument in `RESULT.md`.
