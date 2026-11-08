---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For uniform π∈S_n, conditional on B_i=1, the first succession value H is uniform in 1..n−1 and the other positions form a random bijection. Counting H that preclude π(j)=j yields positive entries (n−2)/[n²(n−1)(n−2)] when j=1,n,i,i+1 and −2/[n²(n−1)(n−2)] elsewhere. Summing rows gives Cov(F,U)=2/[n(n−1)] with endpoint share (n−1)/n. Two distinct succession events have probability 1/[n(n−1)], even overlapping, by ordered-block counting, so Var(U)=(n²−n−1)/n². For covariance matrix M, endpoint row forces sum x_i=0 and interior rows force x_i=−x_(i−1); alternating vector sums to zero iff n is odd, giving rank n−2 odd, n−1 even. Independently exhaustively enumerated all permutations n=3..7 and checked 110 matrix entries.

## originality

PASS

Published marginal fixed-point/succession set equidistribution is not a same-permutation cross-covariance coupling; published fixed-point/descent covariance uses different B_i. The whole n×(n−1) signed kernel, endpoint fraction, and odd-nullspace are not explicitly supplied by examined results, subject to uninspected older joint enumerators.

## value

PASS

The known marginal equidistribution makes the dependence within one permutation a natural unanswered coupling question. The exact signed kernel exhibits boundary-dominated positive aggregate dependence and a parity-specific invisible linear contrast, a structural full-matrix classification rather than a sample-size table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
