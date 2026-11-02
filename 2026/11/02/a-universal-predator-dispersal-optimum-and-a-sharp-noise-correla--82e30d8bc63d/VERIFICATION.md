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

# Reproducibility notes

Run `python verify.py` with Python 3.10 or later; no nonstandard dependencies are required. The program reconstructs the full four-dimensional drift and diffusion covariance matrices and independently solves their stationary Lyapunov equations. It checks 3 exact rational comparisons and 200 seeded numerical cases against the analytical modal formula, 120 additional exact-optimum and gain identities, and spatial-correlation and predator-noise boundary cases. The deterministic seed is embedded in the program.

Proof of uniqueness for infinitely many parameter values is analytical, relying on the positive denominator and the sign of a quadratic derivative numerator. Numerical checks are supporting evidence only. The statement concerns stationary centered Gaussian deviations of the linear system; neither the code nor the proof validates nonlinear ecosystem-level outcomes.
