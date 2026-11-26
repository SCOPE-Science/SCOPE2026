---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The cycle resolvent A=(I+a(I−P))⁻¹ is strictly positive and stochastic by the geometric series. Hence 2A−I preserves row sums and is positive when a<1. Direct cyclic convolution gives the stated diagonal cutoff for n=3 and all-positive square for every a>0; the n=2 rational entries are positive. For fixed n, the inverse of I−P on the zero-sum subspace has forward coefficient (n−3)/(2n). For even m, expanding the nontrivial multipliers via log(−ρ)=−2/[a(1−λ)]+Oₙ(a⁻²), then exponentiating, gives a forward coefficient −(n−3)q/n+Oₙ(q²+q/a), q=2m²/h. This holds uniformly over the dyadics with q bounded by a small constant as h grows (a then diverges uniformly), so it rules out every such dyadic, not just a fixed power or a subsequence. The unsquared large-step diagonal tends to 2/n−1. At the first dyadic above C√h, q stays in a fixed compact positive interval and the nonconstant multipliers have modulus e⁻ᑫ+o(1) uniformly. For sufficiently large C this makes each entry differ from 1/n by less than 1/n. At n=4, inversion using λ=i,−1,−i gives a minus sine for the forward entry, and the other three limiting entries are strictly positive for q>0. The forward sign is that of eᑫ−1−2 sin q, strictly convex on (0,π) with negative initial derivative and strictly positive for q≥π, proving the unique strictly positive threshold. Independent exact rational arithmetic reproduced all four witness numerators and their sum; Decimal bisection reproduced 0.9777603734668504137… .

## originality

PASS

Credit the exact overlap in the one-factor result and the overlap in fixed-power classification. The supported distinct part is the uniform-in-budget half-logarithmic minimum for fixed n≥4 and the four-cycle limiting profile and critical constant. The inspected fixed-power laws and general matrix-exponential methods do not determine these coupled limits.

## value

PASS

The calculation addresses a concrete structural failure: a stochastic row sum does not preserve the qualitative positivity of a Markov approximation. The budget law distinguishes the least necessary scaling order from an easy sufficient linear subdivision count, and the explicit four-state threshold makes the first nontrivial regime quantitatively testable. This is a positivity result, not an accuracy or cost-optimality guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
