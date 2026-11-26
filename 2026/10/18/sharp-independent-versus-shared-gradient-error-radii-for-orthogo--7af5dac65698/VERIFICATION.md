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

The directional derivatives along −p are −a p₁ and −b p₂. Below the independent radius, the endpoint x-order and reverse y-order are strict; every segment point also has positive coordinate sum, since each endpoint's sum is at least min(a,b)−sqrt(2)δ>0. An interior projection is therefore along the positive normal. For an endpoint projection, the variational inequality and the strict endpoint orders force the other coordinate to be positive once the coordinate facing its true gradient is positive. The half-small-norm witness is a horizontal or vertical segment; pushing the relevant endpoint slightly past the axis, while tilting the segment so that the endpoint stays optimal, yields strict ascent at any larger allowance. For shared errors the fixed normal (b,a) has positive inner product with the whole translated segment below d₀=ab/sqrt(a²+b²); endpoint variational inequalities cover cases when the normal foot leaves the segment. At equality translating by −p₀ sends the unperturbed interior foot to zero, and translating by −(1+ε)p₀ sends it to −εp₀, still its interior foot. The ratio simplifies to 2max(a,b)/sqrt(a²+b²) with the claimed endpoint behavior. Independent replay `python3 /workspace/branches/independent-replay.py 2` passed 6,542 exact rational below-threshold grid checks and exact equality and above-threshold witnesses in both regimes. The proof supplies the universal claims.

## originality

PASS

Neither the strongest matching catalogue records nor the examined primary MGDA statements establish this sharp comparison of independent bounded errors and identical translations relative to strict descent against the true gradients. Known projection geometry supplies the variational setup but does not state or supply both exact robust thresholds without the special sign and endpoint analysis. This is a bounded comparison, not a priority determination.

## value

PASS

This isolates the exact price of allowing distinct rather than identical errors for a standard multiobjective direction rule, even when the two per-gradient budgets are the same. The comparison is pointwise and idealized but substantive: the sharp radius changes by a factor between sqrt(2) and 2, and the explicit adversarial bound is not just a continuity estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
