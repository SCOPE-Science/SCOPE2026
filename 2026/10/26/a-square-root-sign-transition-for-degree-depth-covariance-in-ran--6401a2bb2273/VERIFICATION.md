---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For independent uniform parents P_t in {1,...,t−1}, the ancestor event that t lies above the last vertex has probability 1/t for t<n, independently of P_t; the mixed indicator covariance depends on 1+H_(j−1)−H_(t−1). Summing t>j and discrete summation by parts gives Cov(X_(n,j),D_n)=1/j−sum_{t=j}^{n−1}t^(−2), including j=n−1. Direct subtraction gives 1/[j²(j+1)]>0, exact endpoint signs and at most one zero. The inverse-square Euler–Maclaurin tail gives j_+(n)/sqrt(n)→1/sqrt(2), profile n C→1−1/(2c²), and lattice correction 2sqrt(2)(beta−1/6). Independent exact enumeration of all parent arrays n=3..8 rechecked all labels; finite data is not an infinite proof.

## originality

PASS

Best-of-knowledge new age-dependent sign transition for the covariance of a specified vertex outdegree with newest vertex depth, not root degree versus aggregate path length. Same mathematical model degree/depth publications concern a different joint variable or scaling and do not imply the finite identity. No absolute priority guarantee.

## value

PASS

An exact two-statistic dependency profile on a fundamental random tree reveals a nonobvious monotone sign inversion at label sqrt(n/2) and a sharp lattice correction. This is a natural covariance invariant across all labelled vertices, not an arbitrary sampled constant; it can inform joint-degree/depth asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
