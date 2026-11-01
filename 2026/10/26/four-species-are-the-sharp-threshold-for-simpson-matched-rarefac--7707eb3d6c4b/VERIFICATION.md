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

Direct iid discovery-indicator calculation gives R_p(k)=sum_i(1-(1-p_i)^k), and Simpson matching forces R_p(1)=R_q(1) and R_p(2)=R_q(2). For m<=2, first two elementary symmetric power sums determine the unordered frequency multiset and all curves coincide. For m=3, x_i=1-p_i and y_i=1-q_i have common e1,e2; write E_x=1-e1 z+e2 z²-e_x z³, E_y analogous. Because G_x(z)=sum_i(1-x_i z)^(-1)= (3-2e1 z+e2 z²)/E_x, the exact identity G_y-G_x=(e_y-e_x)z³ G_x/E_y has strictly positive coefficients beyond z³ up to the fixed sign of e_y-e_x, unless both curves coincide. No finite grid is used for this all-k proof. For the four-species vectors, sum numerators 21 and square sums 153; independent exact integer checks verified Delta_k=2*19^k+13^k+12^k-20^k-17^k-15^k-11^k, positive k=3..7 and negative k=8..99, while the rigorous tail for all k>=14 follows 20^14>2*19^14 and 17^k+15^k>13^k+12^k. Extension to every m>4 by half-scaling and adding common positive species preserves Simpson equality; k=3 difference scales by 1/8 and eventually the unmatched p rarest species dominates negatively. The analysis concerns expected richness under independent WITH-replacement draws only, not empirical realized richness.

## originality

PASS

The expected-richness identity and the existence of crossing species-accumulation curves are classical, including Lande–DeVries–Walla and Thompson–Withers; those earlier studies compare different true species counts or Simpson values rather than impose both exactly equal. The 2013 Chao–Wang–Jost methods derive accumulation curves and entropy/discovery properties but do not give the sharp three-vs-four fixed-Simpson ordering dichotomy. Algebraic power-sum and majorization-order theory may subsume part of the no-reversal argument under different terminology, which is retained as a real bibliographic risk. The claim is not that curves cross for the first time in ecology but the sharp minimal support with equal Simpson index and exact integer phases.

## value

PASS

Matched species count and Gini–Simpson index fix the asymptote and initial two-draw expected richness yet do not fix ranking for later sampling effort. A sharp minimal species count, universal no-crossing proof at smaller supports, and explicit rational witness with exact all-k sign intervals form a motivated biodiversity-ordering theorem; it illustrates a substantive limitation of summary diversity indices without making empirical inference or sampling-confidence claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
