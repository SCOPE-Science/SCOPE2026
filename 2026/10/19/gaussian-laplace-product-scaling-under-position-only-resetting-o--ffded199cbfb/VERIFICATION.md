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

Run `python verify.py` with NumPy and SciPy installed. The program evaluates 43 numerical and algebraic assertions covering:

- independent finite-grid Gaussian-covariance determinant approximations to the exact conditional Feynman–Kac characteristic function;
- convergence of exact finite-time characteristic functions toward the Gaussian–Laplace product transform;
- independent age integration for the finite-time variance;
- the deterministic mean-diffusivity analogue and its Laplace transform;
- explicit quadratic-coupling upper bounds;
- Gaussian-Hermite quadrature for the mixture transform, numerical evaluation of the density cusp and sharp tail;
- Gaussian-times-Laplace moments, variance, kurtosis and the deterministic comparison.

The program completed all 43 checks. Quadrature approximations cannot establish exact continuum identities or asymptotics; those are established by the displayed stochastic coupling, Feynman–Kac equation, and analytic saddle-point proof. No independent audit has been performed.
