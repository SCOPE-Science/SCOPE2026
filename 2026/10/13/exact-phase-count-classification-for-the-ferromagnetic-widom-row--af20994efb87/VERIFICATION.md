---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The claimed fixed point equations for k>=4, 0<theta<1, a=lambda^(1/k) have exactly one positive symmetric solution: phi(x)=x(1+2x^k)/(1+(1+theta)x^k) is strictly increasing. A nonsymmetric pair u>v is reversibly equivalent to v^k(B_r-theta C_r)=1 with r=u/v. Setting r=exp(2t) gives q(t)=[sinh(t)/(sinh((k-1)t)-theta*sinh((k+1)t))]^(1/k), u=exp(t)q, v=exp(-t)q, and activity Lambda(t). The admissible domain theta<sinh((k-1)t)/sinh((k+1)t) exists only for theta<(k-1)/(k+1). For t>0, g_s=s*coth(st)-coth(t) has strictly positive first and second derivatives in s. Increasing positive discrete differences imply k(g_(k+1)-g_k)>g_(k-1). The logarithmic Lambda derivative has a positive affine numerator in eta=(k+1)theta/(k-1), checked at both endpoint values. Thus Lambda increases from lambda_c=((k+1)/k)^k/(k-1-(k+1)theta) to infinity, producing precisely one nonsymmetric swap-pair above threshold and no pair at or below it. Independent direct substitution and sampled monotonicity checks at k=4,5,9 corroborated, but the infinite conclusion is analytical. The result counts only positive translation-invariant boundary-law solutions/splitting Gibbs measures in the source correspondence.

## originality

PASS

The model-identical 2019 Kissel–Külske–Rozikov paper proves one/three counts for k=2,3, provides only partial lower bounds for k>=4, and explicitly states its Conjecture 1 demanding exact one/three counts. Here the missing all-k upper bound follows from reversible hyperbolic ratio elimination and a convexity-based strictly increasing activity curve. Neither the unrelated published Widom–Rowlinson finite graph-metric partition-function record nor the later dynamic Gibbs/non-Gibbs work implies the full fixed-point count. An unindexed later proof of the conjecture remains a historical priority risk.

## value

PASS

Resolving a stated exact phase-count conjecture on a natural statistical-mechanics tree model for every unresolved tree order is independently useful. The explicit global branch and onset curve remove a significant distinction between at least-three and exactly-three splitting Gibbs measures without extending to all Gibbs measures, periodicity or extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
