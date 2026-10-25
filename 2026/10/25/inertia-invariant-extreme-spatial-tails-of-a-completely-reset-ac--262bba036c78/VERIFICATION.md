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

# Verification details

The included standalone `verify.py` was extracted and executed using Python, NumPy, and SciPy. It performed 449 deterministic assertions. The checks include Fourier-tridiagonal principal eigenvalues across two angular diffusion values, three propulsion values and two translational diffusions; strict positive-root checks for seven or more reset rates; numerical convergence as the Fourier truncation increases; evenness and variational eigenvalue bounds; and correct sides of the exponential-moment threshold. A separate high-accuracy exponential-age quadrature confirmed the exact passive Gaussian covariance term, while independent small- and large-reset parameter sweeps checked the two asymptotic regimes.

The calculation **does not numerically prove** the infinite-mode principal-eigenvalue theorem, the Feynman–Kac asymptotic, or the far-tail logarithmic limits. Those statements rely on the analytic derivations in `RESULT.md`. The variable-heading and fixed-heading reset conventions alter spectral coefficients but not the leading eigenvalue. No independent external mathematical validation was performed.
