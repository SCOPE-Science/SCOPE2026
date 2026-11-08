---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For b>1 and -1<N,D<1, each alpha_j=sqrt((1+Nq^j)/(1+Dq^j)) is strictly positive and tends geometrically to 1. Beta_k=product_{j<k}alpha_j converges to P>0, so diagonal X e_j=beta_j e_j is bounded/invertible with W X=X S. If N>D the decreasing weights yield ||W^k||=beta_k, whence every invertible intertwiner has condition at least beta_k and then P; if N<D the increasing contractive weights have m(W^k)=beta_k and the S-isometry similarity gives condition at least 1/beta_k, then 1/P. In both cases the diagonal X attains, including N=D. Euler–Maclaurin applied to f(x)=log[(1+Ne^-x)/(1+De^-x)] with integrable derivatives gives log P=(Li2(-D)-Li2(-N))/(2h)+f(0)/4+O(h), h=log b, and both terms have common sign. With N=d+tau h, D=d, uniform Taylor expansion gives log P ->(tau/2)log(1+d)/d, with d=0 continuously 1. Independent finite product computations confirmed order-of-magnitude for three parameter pairs at b=1.1 and 1.01. The proof is exact operator-power and Riemann-sum analysis, not numerical sampling.

## originality

PASS

Best-of-knowledge accepted: primary comparisons and actual database queries distinguish the final precise invariant from prior definitions, general bounds/algorithms, and related properties; residual literature access and equivalent-formulation risks are recorded explicitly. No absolute historical priority is certified.

## value

PASS

The least norm condition number of a bounded intertwiner is a natural operator-theoretic invariant beyond a yes/no shift similarity criterion; the exact q-product and singular h^-1 dilogarithmic growth quantify severe instability near b=1. The O(h) parameter-coalescence crossover gives a sharp finite regime for an independently studied GRWS family, meaningful even without a theorem for nonmonotone shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
