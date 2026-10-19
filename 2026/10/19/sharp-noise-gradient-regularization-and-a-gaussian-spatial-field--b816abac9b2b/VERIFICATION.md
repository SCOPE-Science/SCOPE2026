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

# Verification of the mathematical finding

The exact finite covariance is given by the stochastic integral identity in `RESULT.md` Eq. (1). It is a consequence of the explicit drift exponential and Itō isometry, not an empirical guess. Substitution into the continuous stationary Lyapunov equation
\[
(-kI+J_N)C+C(-kI+J_N)^\mathsf T+2D\,\operatorname{diag}(1^{-\beta},\ldots,N^{-\beta})=0
\]
provides a second algebraic check. A positive damping \(k>0\) makes the unique stationary covariance well-defined. The central-binomial Stirling asymptotic and the global binomial-mass bound are used in the rigorous variance and critical-window limits. The Gaussian field claim is limited to convergence of finite-dimensional distributions.

## Reproduce

Run `python3 VERIFIER.py` in the directory with the embedded files. It requires only the Python 3 standard library. It completed **1,864 deterministic assertions**: exact rational Lyapunov checks for \(2\leq N\leq8\), three distinct dampings and three integer bath exponents; numerical comparisons with the covariance integral in the critical window; a sharp logarithmic increment check; and small-lag kernel asymptotics. No simulations, finite tests, or log records are used as substitutes for the analytic infinite-family proof.

## Scientific and validation limits

The spatial profile is exactly a power law and the drift is an open directed Jordan chain. The critical-window statement does not assert tightness or convergence in a continuous-path topology, nor does local second-moment scaling identify a fractional-Brownian process. Some earlier generalized stochastic convolution theory could contain an implicit form of part of the limit. Independent audit has not been performed.
