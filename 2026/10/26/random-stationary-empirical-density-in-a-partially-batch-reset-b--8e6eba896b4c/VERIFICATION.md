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

For each fixed k and finite event window, without-replacement hypergeometric selection tends in total variation to independent Bernoulli(alpha) marks; geometric tails control the infinite window. Conditional on the common Poisson inter-event durations, independent Brownian motions yield k-particle limits nu^{⊗k}, nu=Σ alpha(1-alpha)^j N(0,2D T_j). Conditional exchangeability gives mean-square empirical convergence. Uniform eighth moments of the tagged thinned-clock Gaussian mixture justify products of squares, so the second moment M_N converges in L² to 2D Σq^j E_j. The Laplace product and cumulants follow from independent exponentials; triangular-array Lindeberg with maximal weight sqrt(alpha) and variance→1/2 gives the sequential CLT. The log-Laplace sum establishes the quadratic small-ball exponent with matching small-value event bound. All claims are stationary and sequential, not temporal or joint-N-alpha process assertions.

## originality

PASS

Earlier de Mauro–Majumdar–Schehr (2026) establishes the same Brownian gas and exact marginal/correlation formulas, and fully synchronized resetting yields a common-noise mixture. The surviving claim is the explicit conditional random empirical-measure limit for interior fixed-fraction batches and its full-moment perpetuity, not the batch-reset model, pair correlation, independent general propagation of chaos, or geometric-series small-ball theorem. No direct dominating published statement found in bounded Resultary and primary searches; priority qualified because supplementary sections and all related models were not exhaustively inspected.

## value

PASS

The stationary empirical distribution of a noninteracting gas is a natural macroscopic observable. Its non-self-averaging random limit at fixed positive reset fraction and exact energy perpetuity distinguish a shared-clock phase from ordinary deterministic law-of-large-numbers behavior. This is not simply recomputing the known two-point covariance, because it identifies the entire random weak limiting measure and sequential Gaussian crossover. The precise full-measure law could be reused in later observables and inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
