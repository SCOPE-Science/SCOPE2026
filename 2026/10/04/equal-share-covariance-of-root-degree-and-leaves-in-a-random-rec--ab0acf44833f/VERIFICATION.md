---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The leaf event for label \(i\) has probability \((i-1)/(n-1)\). For \(j>i\), deleting the forbidden parent-choice factor gives \(\operatorname{Cov}(A_j,Y_i)=(i-1)/[(n-1)(j-1)(j-2)]\); for \(j\le i\) independence gives zero. Summing over \(j\) telescopes to the labeled-leaf formula; summing over \(i<j\) gives exactly \(1/[2(n-1)]\) for every \(j\ge3\), and summing over arrivals gives the global covariance. The root-degree variance follows from independent Bernoulli attachments; the leaf variance follows from the exact one-step leaf recursion. A fresh independent enumeration of all parent sequences through \(n=7\) reproduced the global and equal-share covariances exactly; the infinite/family claim rests on the analytic calculation, not enumeration.

## originality

PASS

Best-of-knowledge originality survives. The classical random-recursive-tree literature inspected treats the leaf process, large deviations, or degree-count vectors, not the distinguished root degree jointly with the total leaf count. Targeted semantic and web searches did not locate the exact labeled-leaf covariance profile or the equal-share arrival identity. The remaining risk is older mixed-moment literature under different recursive-tree encodings.

## value

PASS

The exact mixed moment links two basic but differently scaled statistics of a canonical random-tree model. The constant per-arrival contribution and linear labeled-leaf profile reveal structure not visible from the marginal laws and give a reusable finite-n identity, so this is a motivated probabilistic result rather than a routine marginal recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
