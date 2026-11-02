---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For |δ|<1/3 nonzero, uniform X1 and iid increments Y_t in Z/3 with P(0)=1/3, P(+1)=1/3+δ, P(−1)=1/3−δ define a strictly positive stationary ergodic chain. Under IID uniform X_t, the change of variables to X1 and all increments is a bijection preserving their iid uniform distribution. Thus nonzero-step indicators are iid Bernoulli(2/3) under both laws and R_n=1+Bin(n−1,2/3) exactly. The conditional-count plug-in runs center is 2n/3+O_P(1) and variance 2n/9+o_P(n); CLT/Slutsky give asymptotic N(0,1). The transition operator on the zero-sum subspace has eigenvalues ±i√3 δ; even-lag covariance summation yields factor cδ=(1−3δ²)/(1+3δ²)<1; the finite-state CLT gives H_n⇒cδ χ²_2. The Bonferroni union bound therefore gives limsup rejection ≤α/2+(α/2)^(1/cδ)<α. A signed transition statistic has mean 2δ per increment and is consistent. Independent rational enumeration for n=2..6 reproduced exact run laws, directional moments and Pearson expectations. No exact limiting union probability is asserted.

## originality

PASS

Best-of-knowledge original versus closest accessible statements, with real Resultary and primary-source comparisons; failed search is not novelty proof and uninspected plausible literature is recorded, not declared noncovering.

## value

PASS

This precisely identifies a natural published runs-plus-frequency independence test which remains asymptotically conservative against an irreducible dependent process with correct marginals, and exhibits a consistent directional repair statistic. The defect concerns an actionable statistical test and its blind spot, not an arbitrary model slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
