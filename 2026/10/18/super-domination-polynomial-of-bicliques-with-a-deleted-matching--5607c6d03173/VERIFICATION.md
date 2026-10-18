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

## Reproduction

Use Python 3 standard library and run `python check_super_match.py` in the directory containing this document. The complete expected output is in `verification_output.txt`. The checker reconstructs each bipartite graph with exactly the specified deleted matching edges, enumerates every vertex subset, independently tests the open-neighborhood witness condition, and compares counts for every pair of omitted-side sizes.

It covers all \(3\leq a,b\leq7\) and all \(0\leq t\leq\min\{a,b\}\), totaling \(130\) graph profiles and \(407040\) tested vertex subsets. This finite verification is not a proof for unbounded parameters; the separate combinatorial argument proves the full theorem. The polynomial coefficients and exceptional \((3,3,3)\) boundary are explicitly included in both sources of computation.

Self-review is documented in `REVIEW.md` and `AUDIT.json`; no independent audit has been performed.
