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

The accompanying `verify.py` independently computes the exact finite-state greedy matching probability from two representations: state reduction to the number of intact deleted pairs and singleton vertices, and direct dynamic programming on actual uncovered vertex subsets. Its rational results agree for \(n=1,2,\ldots,7\). It also checks finite one-pair moment brackets and a conservative two-pair moment bound for \(5\le n\le18\). A numerical recurrence through \(n=1000\) illustrates convergence of \(nP_n\) toward \(3/4\), but does not establish the infinite-size theorem.

The analytic proof establishes the asymptotic result for all integers \(n\ge2\) with the displayed finite-state recurrence. The proof of the rate uses a rare-pair decomposition at an intermediate scale and bounds on the first two factorial moments. The source comparison includes a full open preprint of one close greedy-matching paper; full text access to some older papers was unavailable. No independent validation has occurred.
