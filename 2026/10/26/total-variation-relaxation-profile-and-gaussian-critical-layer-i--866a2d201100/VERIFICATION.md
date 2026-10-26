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

# Deterministic verification and limits

Run `python verify.py` with Python 3, SciPy and NumPy. The program includes 60 independent numerical quadrature checks of the exact finite-chain characteristic-function transform, 8 precritical checks of numerically integrated central-interval total variation at increasing indices, 12 critical-window profile checks, 3 finite-index Gamma-tail coupling inequalities, and 1 exact critical coefficient check: **84 deterministic checks passed** when replayed from the finalized file directory.

The procedure integrates over the published Gamma random-clock representation. It numerically locates the single positive crossing of the finite-index signed spatial density and integrates the central mass difference; the analytic monotonic-ratio proof establishes uniqueness for all indices and positive times, rather than relying on those root finds. Approximations at finite indices are not infinite-limit proofs. The paper's precritical formula and critical n-dependent profile are proved by the accompanying analytical L1 concentration and variance-derivative arguments.

The Fourier check uses regularized incomplete Gamma functions and quadrature in dimensionless units; diffusivity and reset-rate cancel after the indicated rescaling. There is no randomness or external network access in the program.

There is no independent audit or external validation in this package.
