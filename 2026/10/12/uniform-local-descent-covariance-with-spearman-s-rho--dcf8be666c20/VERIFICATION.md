---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: For n>=2 and every i=1..n-1, using L=sum j*pi(j), D=2 sum j^2-2L. A uniformly selected unordered pair conditioned to be a descent has maximum 2(n+1)/3, minimum (n+1)/3, and other positions have mean (n+1)/2. Hence conditional L shift=-(n+1)/6 at every i, giving Cov(I_i,D)=(n+1)/6 and Cov(I_i,R)=-1/[n(n-1)]. Summing and using standard exact variances gives Cov(A,R)=-1/n and the stated correlation. Checked normalization and n=2 boundary, and independently enumerated exact rational permutation statistics for all n=2..7 and every i (not substituted for infinite proof).

## originality

PASS

PASS best-of-knowledge: Conger concerns Eulerian descent distribution conditioned by the first value, not Spearman squared displacement; Jiang treats Spearman/distance asymptotics without local descent indicators. Resultary retrieval returned incidence inversion or fixed-point/descent statistics, not this covariance. Local position-invariance and global n^-1 constant not implied by inspected statements; possible older alternate notation remains residual risk.

## value

PASS

PASS: An exact position-uniform covariance and conditional rank-correlation shift links a local Eulerian test statistic to a global rank-distance test statistic in the canonical uniform-permutation null, distinguishing boundary positions. The exact first-order decay constant and finite-n identity are natural reusable facts beyond a standard variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
