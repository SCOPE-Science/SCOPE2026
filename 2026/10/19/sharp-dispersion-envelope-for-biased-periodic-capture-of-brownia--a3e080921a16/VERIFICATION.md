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

The analytic statement applies to \(D,L,r>0\) and every gate parameter \(\theta\in[0,1]\). The Brownian variance normalization is \(\operatorname{Var}(\sqrt{2D}B_t)=2Dt\); effective diffusivity is \(\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\). The weak-limit parameter is \(z=L\sqrt{r/D}\). These conventions fix all factors of two in the formulas.

The proof reduces the model to independent pairs of Brownian capture displacement and exponential cycle time, then computes the required reward-duration correlation. The global strict inequality is proved analytically from a derivative factorization and the inequality \(0<(s\coth s)'<\tanh s\). The included Python 3 program `check_dispersion.py` can be run with NumPy and mpmath and passed 246 assertions using a deterministic random seed. Checks include Laplace/geometric reward moments, an independent numerical derivative, gate extrema, the short- and long-rate expansions, and direct cycle simulation. These tests are finite and are *not* an exhaustive proof over continuous parameters or an independent audit.

The proof does not treat finite-time noninstantaneous returns, irregular target placements, non-Brownian motion between captures, or non-Poisson waiting times. The distributional time-to-return correlation is essential: deleting it produces a generally incorrect diffusivity. Large-rate behavior is singular when a basin boundary passes through a lattice site. Priority relative to an unlocated general theorem remains a limitation.
