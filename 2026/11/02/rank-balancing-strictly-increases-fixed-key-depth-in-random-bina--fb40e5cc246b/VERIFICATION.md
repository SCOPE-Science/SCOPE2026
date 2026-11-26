---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Conditional on the searched key's uniform priority u, its ancestors on each side are the lower records among independently retained priorities below u. At ranks i and i+1, share a Bin(i-1,u), a Bin(n-i-1,u), and one Bernoulli(u) which is assigned to opposite sides in the two marginals. When the extra trial succeeds, the incremental record success probabilities are 1/(x+1) versus 1/(y+1), multiplying the same symmetric nonnegative threshold factor P(C_x+C_y=t-1). Pair x<y with its transposition: the binomial likelihood ratio in the larger trial count is increasing, so every combined contribution is nonnegative, including pairs outside the smaller support. For i<n/2 the strict pair (0,1) works at t=2; at larger t use (0,t-1) if i=1, otherwise (i-1,n-i-1), since a positive-length record count has full support from 1 to its length. These pairs work for every 0<u<1. Root probability 1/n and maximal depth n-1 give the endpoint equalities; reflection gives the even central equality. The expected depth is H_i+H_{n+1-i}-2 by summing inverse interval lengths (ancestor probabilities), and ordered laws have W1 equal to their mean difference via quantile coupling. The uploaded verifier was inspected, not executed; VERIFICATION.md records 6,500 exact assertions, including exhaustive insertion through n=8 and recurrence-based checks through n=24. All-size strictness is established analytically.

## originality

PASS

Pass for the supported adjacent-rank, strict all-interior-threshold comparison. The individual marginal laws and harmonic means are classical, and the W1 formula is a consequence of the ordering, not a separate new distribution theorem. The strongest inspected overlaps give either exact marginal input or a different conditional order, not this joint statement about ranks.

## value

PASS

This compares the full finite search cost by key rank, not just its average or a central-limit regime. It answers whether every attainable nontrivial deadline is less likely to be met toward the center, even at the extreme tail, and isolates the exact exceptional thresholds and central symmetry. The method controls competing changes of the two random record counts; the transport calculation is useful but secondary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
