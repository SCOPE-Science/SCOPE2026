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

# Exact verification and boundaries

The included `verify_gap_law.py` was run using Python's standard library only. `verification_output.json` contains the actual result. The checker exhausts all permutations and marked position sets for \(2\leq n\leq7\), checking each conditional inversion mean against the closed formula and independently aggregating moments of the increasing-subsequence count and the inversion statistic. It also checks the sharp minimum and maximum of the weighted gap across all selected sets, and computes the \(n=8,k=4\) test values using exact rational arithmetic.

All cases returned `PASS`; this checks finite examples only. The argument for all sizes depends on the analytically derived uniform-relative-rank comparison and on the exact identity for the interior gap contributions. Independent audit, external formalization, and broader historical-priority certification have not been performed.
