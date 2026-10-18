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

For every n>=2 the four closed-neighborhood inequalities L>=1, R>=1, L+beta>=1, R+alpha>=1 are logically equivalent to signed domination: ordinary clique vertices give the first two, bridge vertices the latter two. For even n parity forces L,R>=2 and extra constraints are vacuous; independent binomial choices give W=P_n^2 and gamma_s=4. For odd n=2q+1 condition on both endpoint labels, giving disjoint A^2+2BC+D^2 enumerators. Minimum odd weight 2 requires both clique sums 1 and both bridge labels +1; multiplicity C(2q,q)^2. Independently enumerated ALL 2^(2n) signings and weight coefficients for each n=2..8 (total 87376) and confirmed both formulas, but unrestricted proof is symbolic.

## originality

PASS

Same barbell graph and same closed-neighborhood signed function convention as classic signed domination, but full signed weight enumerator is not implied by the ordinary domination polynomial D(B_n,x) from Jahari–Alikhani or Zelinka's signed scalar K_{p,q} results. The parity-dependent bridge effect is genuinely outside both examined statements. Best-of-knowledge originality with unindexed graph-family enumeration residual risk.

## value

PASS

Full weight enumerator, not just scalar gamma_s, is an exact structural invariant for the natural symmetric barbell family; the parity of clique size controls whether adding a single bridge changes any signed dominating assignments, contrary to ordinary-domination edge irrelevance. Coefficientwise formula and minimal layer counts offer meaningful function enumeration beyond a textbook scalar optimization and could serve future domination polynomial comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
