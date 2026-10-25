---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For every nonempty block S of K_{m,n}, a paired-dominating set is exactly one with equal positive part populations, because K_{a,b} has perfect matching iff a=b>0 and then dominates K_{m,n}. Nonpaired blocks have nonzero signed imbalance; partners iff their imbalances sum to 0. Therefore each distinct |d| yields exactly one complete bipartite PCG component with p_d,q_d>=1; the feasibility m=t+sum d*p_d, n=t+sum d*q_d is necessary and constructive (allocate t neutral pairs to a block). Distinct positive d each use at least d vertices from BOTH sides; sum d>=c(c+1)/2 gives the sharp maximum c and all c by explicit pure-block construction. Equality at m=n=T_c forces sizes 1..c and c! labeling quotient, giving (T_c!/prod j!)^2. The block-assembly bivariate labeled EGF treats each present sign as a nonempty SET of blocks, counts components u and blocks z without witness overcount. Independent enumeration of unlabeled set partitions of K_{2,4} and K_{3,3}, direct domination/matching checks, recovered 20 and 50 admissible partitions, with precisely nine 2-component partitions for K_{3,3}, confirming triangular extremal formula.

## originality

PASS

Best-of-knowledge original as a realization/enumeration theorem for every PCG(K_{m,n}) isomorphism type and its fragmentation profile. Samadzadeh, Mojdeh and Nadimi introduce paired coalition and show PC(Kmultipartite)=total vertices: a scalar maximum number of blocks, not a classification of PCG connected components or all partition coefficients. Published paired-domination polynomials enumerate balanced sets, not partitions into nonpaired blocks with signed partners. Primary source material inspected and Resultary comparison contain no implication of distinct-magnitude triangular extremum or bivariate EGF.

## value

PASS

A full realization criterion for a natural coalition graph operator and an exact quantitative fragmentation law answer an intrinsic structural question beyond the scalar coalition number. The sharp triangular cutoff identifies the minimum resource cost of c distinct partner-imbalance magnitudes; the two-variable labeled generating function captures exact global partition data and can be used to recover many invariants. Distinct full-space classification and EGF are mathematically motivated, not a small arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
