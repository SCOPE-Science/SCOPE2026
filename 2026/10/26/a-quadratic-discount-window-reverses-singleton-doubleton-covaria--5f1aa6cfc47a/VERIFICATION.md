---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The EPPF/Chinese-restaurant predictive law gives exact marked singleton/doubleton probabilities, from which μ1,μ2,μ12 and the ratio R_n=μ12/(μ1 μ2) follow by cancellation. The exact Ewens boundary is R_n(0)-1=2(1−θ)/[n(n+θ−3)]. The logarithmic derivative at zero is 1/θ−2/(n+θ−3)−1/(n+θ−2), tending to 1/θ. Its second derivative is a signed sum of reciprocals squared uniformly bounded for α in [0,1/2] by a θ-dependent finite series. Thus g_n=log R_n is strictly increasing on one fixed small interval for all large n, crosses zero once for θ>1, and Taylor expansion at α=O(n^−2) gives n²g_n→2(1−θ)+c/θ. Since μ1→θ and μ2→θ/2, the stated covariance limit and root scaling follow. Independent exact-rational recursion of ordered block sizes agrees with all three moments at five n, three θ and two α values. This is a moving-boundary result, not an all-discount sign classification.

## originality

PASS

Best-of-knowledge independent claim-versus-prior implication comparison: Published finite EPPF permits recovering input moments, but deriving sharp near-α=0 n^-2 signed covariance and fixed-interval local root needs an additional uniform Taylor derivative analysis. No direct prior implication identified. Closest exact antecedents are explicitly credited and risks retained.

## value

PASS

Singleton and doubleton counts are fundamental natural observables of the same exchangeable partition, and discount α=0 is a distinguished transition to the Dirichlet process. The exact inverse-square window and sign reversal resolve a motivated fine dependence question not captured by the known raw EPPF. The absolute magnitude of covariance is only O(n^−2), explicitly limiting empirical interpretations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
