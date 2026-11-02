---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For independent continuous coordinate marginals, sorting descending X leaves iid Y and makes M_n the upper-record sum. Given A_n=a, K_n counts Y threshold exceedances among the first a ranks. Each record indicator i<=a is independent of the symmetric first-a count; for i>a and j<=a conditional rank symmetry gives Cov(R_i,1{Z_j>t})=-(1-q)(1-(1-q)^(i-1))/(i(i-1)). Summing yields equation (1), and binomial mixing yields (2), with zero endpoint a=0,n. Telescoping a*sum_{i=a+1}^n1/[i(i-1)]=1-a/n and bounding the q-geometric tail give the strictly positive error and bound (4) for all n>=2 and p,q in (0,1), implying (3). Independent exact-rational checks verified all 199 n=2..7 rank cells and 297 grid cases up to n=34, including n=2:-1/16 and n=3:-15/128 at p=q=1/2. Finite checks supplement but do not prove the infinite-domain theorem.

## originality

PASS

Best-of-knowledge original exact mixed covariance between number of planar Pareto maxima and fixed northeast occupancy, including every conditional count, strict sign, universal nonzero limit and exponential finite-sample envelope. The broad primary literature inspected studies mean/variance/limit behavior of the maxima count or maximal-point indicators, not the required cross statistic. Prior permutation symmetry alone does not determine the cross moment.

## value

PASS

The number of Pareto maxima and count exceeding a fixed northeast corner are natural descriptors of a random skyline. Although M_n is independent of each marginal threshold count and even of their pair, it has a strictly negative covariance with their intersection; the exact conditional sign, universal nonzero limit, and exponential error give meaningful structural and finite-sample information. The result is not simply the standard harmonic expectation, a marginal CLT, or a finite table recomputation. The scope is a focused exact statistic rather than a general skyline theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
