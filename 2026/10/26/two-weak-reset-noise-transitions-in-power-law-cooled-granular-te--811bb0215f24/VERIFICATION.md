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
# Reproducibility and checks

The included `verify.py` uses numerical quadrature on the independent rate-one exponential variable to compute stationary moments, the renewal-reward variance, and a separately integrated stationary two-time covariance. At seven nondegenerate parameter choices it tests the Green–Kubo identity and checks covariance positivity at two lags. Two additional parameter sets at resetting rate \(0.01\) check the order of the asymptotic variance. It separately checks \(B_{1/2}=4-\pi\) and positivity of representative constants. All tests pass when run with Python 3 and SciPy.

Critical analytical checks are in RESULT.md: the two-sided Poisson-age decomposition, regenerative reward CLT with exponential-moment bounds, and the \(L^2\) weak-rate limits for three intervals plus the stationary-variance logarithmic boundary. The remaining claims are strictly asymptotic statements. Quadrature and finite numerical comparisons cannot prove the limiting asymptotics, publication novelty, or an independent scientific validation. The model excludes microscopic stochastic granular fluctuations and the proof does not treat joint long-horizon/low-reset limits.
