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

The standalone checker `verify_cyclic_subseq.py` uses standard-library dynamic programming, independently from the weak-descent counting argument. It enumerates and checks all scattered subsequence multiplicities for \(q=2\), \(1\le m\le8\); \(q=3\), \(1\le m\le5\); \(q=4\), \(1\le m\le4\); and \(q=5\), \(1\le m\le3\). It checks the exact maximizing target set for all these cases with \(m\ge2\), verifies the row-sum generating-function recurrence through degree \(36\), and tests strict log-concavity for \(2\le q\le10\) and \(2\le m\le40\).

Actual completed output:

`CYCLIC_PERM_SUBSEQUENCE_PASS full_DP_cases=20 tested_patterns=96595 winning_patterns=76 GF_coefficients=0..36 q=2..5 strict_log_concavity=q2..10,m2..40`

The infinite generalization, root analysis, and entropy rate are proved symbolically in `RESULT.md`; this finite verifier is not an exhaustive proof for unbounded parameters. The result has no independent mathematical audit.
