---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For any compactly supported invariant probability measure the slow increment Δy=-μ(x-(σ−1)) has zero mean, giving E[x]=σ−1. Stationarity of y² expands to 0=−2μ Cov(x,y)+μ² Var(x), hence Cov=(μ/2)Var(x); no fast-map regularity is required. Cauchy–Schwarz gives the sharp variance lower bound. Equality with nonzero Var(x) fixes y−Ey=(μ/2)(x−m) almost surely, and invariance applies this relation at the image point, so x_{n+1}−m=−(x_n−m), y_{n+2}=y_n a.s.; any ergodic nondegenerate equality measure is a two-cycle. The strict correlation assertion correctly excludes zero Var(x), fixed points and period-two equality. Independent hand expansion and exact-rational source-code inspection confirm normalization μ=.001, σ=.322.

## originality

PASS

Best-of-knowledge: original and later same-map primary treatments focus on the slow nullcline, spiking/bursting bifurcations, canards and chaos, rather than an all-compact-invariant-measure covariance determinant and period-two equality classification. The second-moment balance is short and could be independently known under stationary-energy terminology; explicitly retain that originality risk. Resultary did not complete and contributes no negative-search evidence.

## value

PASS

Stationary fast–slow covariance is a natural physical statistic for the canonical Rulkov neuron map. The result gives an exact global consistency law and fluctuation bound across all compact stationary regimes and, crucially, converts equality in a statistical bound into a dynamical period-two obstruction. That motivated structural rigidity exceeds a trivial normalizing observation and is independently useful for comparing simulated regular versus bursting invariant statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
