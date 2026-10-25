---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Root subtrees conditional on either labeled partition (also after forgetting which side is first at a balanced split) are independent uniform PDA trees. Cherry counts add, so the conditional variance is v(k)+v(n-k). Contraction of one and two disjoint leaf pairs yields E C_m=binom(m,2)/(2m-3) and E(C_m(C_m-1))=binom(m,2)*binom(m-2,2)/[(2m-3)(2m-5)], hence v(m)=m(m-1)(m-2)(m-3)/[2(2m-3)^2(2m-5)] for m>=4 and zero for m<=3. The derivative certificates in RESULT.md give v''(x)<0 for x>=3, and v(m+1)>v(m), proving the unique min at k=3 and reduction of maxima to k=1 or k=floor(n/2). The even polynomial P(m)=16m^3-164m^2+393m-270 is negative for m=3..7 and has positive shifted coefficients at m>=8. The odd sixth-degree Q(m) is negative m=3..6 and has positive coefficients after shifting m=7, giving the strict n=15 transition. Independent exact Fraction/SymPy checks confirmed the two exact n14/n15 gaps and the strict extrema for every n=6..300. The analytic parity sign certificates, not this finite sweep, prove all n. Expansion v(x)=x/16-1/32-3/(32x)+O(x^-2) yields asymptotic gap 1/32.

## originality

PASS

Qualified best-of-knowledge originality for the precise final theorem and its stated parameter domain. The four named implication comparisons discriminate known mathematical inputs from the sharp new increment; an unindexed equivalence remains possible. A short formula V_n(k)=v(k)+v(n-k) follows routinely, but neither strict argmin k3, argmax switch n14→15, nor limit 1/32 is stated or automatic without the global comparison and sign proof.

## value

PASS

Cherry counts are a canonical local statistic in phylogenetic PDA trees, and root split size measures balance. Conditional fluctuation extremizers and the sharp n15 reversal answer a natural model question not resolved by the unconditional marginal moments alone. The 1/32 persistent asymptotic advantage adds qualitative meaning beyond a tiny finite curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
