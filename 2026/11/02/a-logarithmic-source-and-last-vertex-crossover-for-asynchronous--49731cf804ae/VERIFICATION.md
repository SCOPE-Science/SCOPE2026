---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 checker.py` with Python 3.10 or later and no third-party packages. The checker evaluates the exact finite-state continuous-time Markov recurrence and an independently derived signed-binomial/Laplace-transform formula with rational arithmetic. For every \(1\le a,b\le9\), it checks both the exact expected completion time and the probability that the last leaf informed lies on the initially informed hub's side. Further exact bounds and the two hub-start mean inequalities bring the exact-assertion total to 369. The program also numerically integrates the independent finite-time CDFs for source-order diagnostics and uses a fixed seed to inspect two asymptotic scalings.

The recurrence and the analytic formula are implemented independently and agree. The finite checker does **not** establish source stochastic ordering for all sizes, nor any asymptotic limit. Those conclusions depend on the printed CDF-ratio proof and exponential-max convergence. Randomized diagnostics are not exact certificates and do not certify originality or independent review.
