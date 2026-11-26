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

For fixed anchor i the blockwise top-coordinate selections are independent and finite-block truncation tends monotonically to A_i(x). Heredity holds using the same anchor, including when a subset no longer meets that block. Anchor 1 takes at least half the mass in every block and all the first block; lattice domination gives the upper bound. Equal mass on each of the first k blocks, uniform within each, gives A_i=1/k+(k-i)/(k2^i) on i<=k and zero thereafter, and maximum (k+1)/(2k); a coordinate vector attains the upper ratio. Thus the completion is ℓ1. For nonzero x, A_i(x) is bounded by the ℓ1 tail from i and hence an anchor attains the norm. Fix it when x_m tends coordinatewise to x with converging norms. Its contribution from j>J is at least 2^-i times the ℓ1 tail there. Subtract the continuous finite-head contribution and take limsup to bound the sequence tails by 2^i times the omitted contribution of x, tending to zero with J. The x=0 case follows from norm equivalence. A bounded sequence admits a coordinatewise convergent subsequence and Fatou gives an ℓ1 limit; finite equinorming supplies the upper bound on the limiting norms and the supremum of finite coordinate seminorms gives lower semicontinuity. Kadec then gives norm convergence. Conversely, a finite norm net and finite selections approximating its members' norms yield equinorming by Lipschitz continuity. In Definition 7, use uniform weights on D=B_i and on a whole B_j beyond any cutoff. Capturing more than half of D forces anchor i; the remote capture then has fraction at most 2^-i, which can be made smaller than any positive γ. This works throughout the source's admissible 0<γ<=1; γ>1 is outside that definition and impossible as a coverage fraction. Theorems 12–13 supply the compactness implication via Theorem 9, not in isolation.

## originality

PASS

The broad separation and its local tail-capture mechanism were already demonstrated by SCOPE-20261018-ee98a8808bdb; do not credit them as new on their own. This record does it for a hereditary family in an ℓ1 renorming with the sharp lower comparison 1/2. The earlier sparse family is strictly smaller even after taking its hereditary closure, and its completed space is not isomorphic to ℓ1. This is a supported distinction in geometry, not a distinction based only on wording or constants.

## value

PASS

The prior sparse example shows that the sufficient directedness condition is not necessary in general. The frozen construction answers the more constrained question in a familiar hereditary ℓ1 setting, where the source also has a contrasting ℓ1-equivalent negative example. The sharp comparison and fixed-anchor control explain why one-set equinorming succeeds in this realization despite the failure of positive uniform capture. The point is not the numerical constant alone or a repeat of the qualitative existence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
