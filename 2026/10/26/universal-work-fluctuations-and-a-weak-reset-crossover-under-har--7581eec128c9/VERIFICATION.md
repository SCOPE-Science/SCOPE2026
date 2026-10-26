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

# Reproducibility and verification

The accompanying source `verify.py` is complete and requires only Python 3 with NumPy. Run `python verify.py` in the directory containing that file. The verified run printed `ALL CHECKS PASS` after six independently sampled Brownian renewal-epoch experiments and three near-weak-reset second-moment comparisons. The simulation uses independent normal samples conditional on independently sampled exponential, Erlang-three and deterministic exploration times. It does not use the derived covariance law to generate increments.

The exact variance checked for each parameter setting is
\[
\operatorname{Var}(W_n)=\kappa^2D^2\left(2m^2+3v\frac{1-a^2}{1+a^2}\right)
\left[n\frac{1+a^2}{1-a^2}-\frac{2a^2(1-a^{2n})}{(1-a^2)^2}\right].
\]
The normalization of the weak-reset limit is \(W_n/(n\kappa Dm)\); for \(n(1-a^2)\to2\), its limiting variance is \(1+e^{-2}\), numerically about 1.1353352832. The finite-size comparisons used \(1-a^2\) equal to 0.05, 0.02 and 0.008. The first comparison differs from the continuum variance by about 0.0299 and decreases toward zero with the step size.

The program tests finite-dimensional consequences only. Analytical proof is required for all integer \(n\), ergodic central limit convergence and the functional weak-reset limit; these proofs appear in `RESULT.md`. The stationary initialization used in simulations is an approximation obtained by burn-in; its squared contraction error is bounded geometrically by \(a^{2b}\) times the initial second-moment difference. Numerical error thresholds accommodate Monte Carlo sampling uncertainty. No external or independent audit is represented by these checks.
