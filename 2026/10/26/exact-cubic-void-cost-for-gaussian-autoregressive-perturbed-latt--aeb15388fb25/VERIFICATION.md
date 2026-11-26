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

The shift yields stationarity: translating by t sends U to its fractional part after adding t and reindexes by the integer part, which preserves the displacement law even conditional on U. Sitewise Gaussian tails give local finiteness. For integer N, a hole requires a squared displacement sum over 0,…,N at least N³/12+O(N²), uniformly in U. Nonnegative correlations give a covariance norm at most Λ by absolute row sums; Gaussian diagonalization gives the stated determinant bound with dimension loss only O(N) at fixed ε. This gives the lower bound on −log V. Conversely the evacuation box forces the protected sites outside, and its center has squared norm N³/12+O(N²) and squared differences O(N²), including the central jump. With both ends zero, expanding the AR energy gives (1−ρ)² times the squared norm plus ρ times the squared differences. The bounded coordinate error changes this energy by O(N²); initial density, volume, and fixed shift restriction have at most O(N) log cost. Dividing by twice the innovation variance gives the matching N³/(24Λ). Conditional on the block and shift, both exterior chains have bounded means and variances, by stationarity and AR(1) reversibility. Entry thresholds grow at least as N+k−1 at distance k, so the sum of conditional tail probabilities is uniformly o(1); no exterior independence is needed. Positivity for all finite L follows by containment in a sufficiently large integer window with positive void probability. Strict inequality from one follows from the positive chance for a single Gaussian-displaced site to land in any positive-length window. Monotonicity gives real lengths and ρ=0 yields the independent constant without a singular step. The recorded exact-rational checks illustrate the algebra; the script was inspected, not run, and the infinite-volume assertion follows from the analytic bounds.

## originality

PASS

The supported distinct claim is the exact positive-correlation AR(1) interval-hole rate. An inspected matching catalogue result covers the independent specialization, and the inspected independent and dependent primary results do not give the sharp constant at positive ρ. The known independent coefficient is not credited as an independent novelty.

## value

PASS

The rate for a stationary rare-event model is motivated before calculation by lattice void estimates and the gap between mixing bounds and iid logarithmic order. For a fixed positive correlation the result determines exactly how dependence changes the cost, replacing marginal variance by integrated covariance. The two sides require a displacement threshold and a path attaining its leading energy while all external sites are controlled. An exact coefficient in a simple correlated benchmark is useful for comparison with future dependent-field bounds; the independent specialization alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
