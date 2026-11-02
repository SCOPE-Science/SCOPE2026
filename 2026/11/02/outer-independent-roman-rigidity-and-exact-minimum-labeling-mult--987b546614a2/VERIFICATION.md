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

# Reproducibility and limits

Execute the included `CHECKER.py` with standard-library Python 3: `python3 CHECKER.py`. It reconstructs each Cartesian product directly, then checks that zero vertices are independent and defended and that the positive-support induced graph has no isolated vertex. Across six clique widths and up to 79 columns, it validates 936 explicit optimal labelings for both path and cycle families. It performs exact unrestricted column-state dynamic programming on 20 small cases, and full three-valued function enumeration on four smaller graphs, including the triangle clique-cylinder. The graph and dynamic-programming tests agree with the scalar minima and with the all-optimal function counts for every tested multiple-of-three length.

Observed final result: `VERIFY_OK: 936 constructed and graph-checked witnesses; 20 unrestricted DP minima/counts; 4 direct all-label graph enumerations`.

The finite computation alone does not establish any assertion for unbounded sizes. The proof derives the bound, constructs valid witnesses for all allowed parameter values, handles the exceptional triangle cylinder, and forces the exact three-column tilings at lengths divisible by three.

Self-review status: passed. Independent audit has not been performed; neither external validation nor publication-priority certification is asserted.
