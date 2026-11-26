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

In rate-one Poisson time, the m=nd/2 edge clocks split independently. If q=e^(−t/m), a vertex is untouched with p=q^d. Each ordered adjacent pair shares exactly one edge, giving joint probability p²/q; each nonadjacent pair is independent. The nd ordered adjacent pairs give the stated variance. Setting all incident-edge untouched indicators at a uniformly chosen vertex to one has the conditional law given that vertex untouched, a valid size-bias coupling because the vertex marginals agree. Its count increment is zero if the chosen vertex was already untouched and otherwise one plus the number of newly untouched neighbours. Thus E|W+1−Wˢ|=p+dp(q⁻¹−1), which with the Poisson first-difference Stein factor yields the finite TV inequality. For u=log n+x≥0, d(e^(u/d)−1) decreases with d, so d=2 is the worst upper bound, including u=0 by equality. Coverage means W=0. Conditional on the sampled edge sequence the time of completion is a sum of K independent mean-one exponentials; the union bound P(K>n log n)=O(1/n) and the conditional variance show the clock changes the normalized time by o_P(1) uniformly. For the mean, the continuous-time centered upper tail is at most e^(−a); the lower tail is at most e^(−a)+2n^(−1/2)e^(−a/2) by the variance bound up to a=log n and zero above it. These bounds also control the boundary terms in the truncated mean, giving uniform integrability and the Euler constant. The conditional mean of the Poisson time is K. At degree one, K is the classical collector of n/2 edges, giving the stated shifted law and harmonic mean. The finite law can depend on topology: C₆ admits coverage by three disjoint edges, but two disjoint triangles need four, so the small-time Poisson coverage probabilities have different leading orders.

## originality

PASS

Credit the exact moment identities to general structured-coupon formulas and the TV computation to the specialization of increasing size-bias Stein bounds; the matching-graph case is classical. The supported distinct contribution is the sharp critical-window and order-n mean classification uniformly over arbitrary simple regular support, including sparse, disconnected, and varying-degree graphs. The strongest prior structured-coupon theorem examined reaches first-order concentration for this full family, and the strongest inspected Gumbel precedents cover subfamilies only. The finite moment calculation and general Stein tool are not independent originality claims.

## value

PASS

The distinction between degree one and degree at least two is a meaningful boundary for dependent two-vertex coupons. The theorem controls the full coverage window and the next mean term uniformly even for bounded-degree or disconnected supports, where the complete-graph group results do not apply. First-order concentration and the exact moments alone would not answer whether the topology changes the limiting profile or the Euler-constant term.

The dated certificate retains the supplied scientific assessment, sources and limitations.
