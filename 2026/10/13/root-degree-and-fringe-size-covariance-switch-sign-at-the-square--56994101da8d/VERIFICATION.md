---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A nonroot vertex v starts a two-color urn with one descendant and v-1 complement vertices, so the beta-binomial weight applies exactly for 2<=v<=n-k+1. Given the membership history, only complement arrivals can attach to the root after v. Their denominator sequence is v-1 through n-k-1, independent of the order of subtree arrivals; including earlier arrivals and v's independent parent gives H_{n-k-1}+1/(v-1). The two binomial sums then give E F_{n,k}=n/[k(k+1)] and E[R_n F_{n,k}]=H_{n-k-1} n/[k(k+1)]+1/k. The crossing exists because b_{n,k} increases strictly from below 1 at k=1 to H_{n-1}>1 at k=n-1. Uniform expansion for k=O(sqrt n) gives Cov=1/[k(k+1)]-1/(2n)+O(k/n^2); the signs at (sqrt(2)±epsilon)sqrt n squeeze the crossing. The exact finite rank is kappa_n as defined, not sqrt(2n); covariance can be zero at the crossing, and k=1 gives the known leaf identity. In a separate finite replay all 5,913 parent vectors through n=8 were compared with exact rational means, covariances and monotonicity; summary /workspace/branches/bab8b9f6-a731-4da8-bbb1-6bfc68c648f9/independent-replay.md. The supplied CHECK.py was inspected, not executed.

## originality

PASS

The supported distinct claim is the exact distinguished-root degree/size-k fringe-count mixed moment for k>=2, with its covariance crossover and scaled limit. Neither the prior leaf boundary nor the marginal square-root transition is passed as new. The strongest accessible primary covariance theorem and closest catalogue findings do not establish equivalent coverage of the supported claim.

## value

PASS

The root outdegree and the full descendant fringe profile are natural complementary tree statistics. The exact mixed profile is a finite-size benchmark and reveals that the direction of dependence changes with size, locating the normalized crossover and magnitude rather than merely identifying a marginal scale. This is useful for studies of joint root/fringe fluctuations even without proving any joint limit distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
