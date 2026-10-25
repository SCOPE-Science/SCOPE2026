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

# Reproducibility checks

Run `python verify.py` with Python 3, NumPy and SciPy. This script reconstructs the drift and diffusion matrices independently, verifies the closed-form stationary covariance against a numerical continuous Lyapunov solution across nontrivial parameter choices, and checks the exact matrix-exponential covariance flow and the short-time Gaussian logarithmic-negativity law. It also propagates a finite Fock-space truncation of the full Lindblad generator to crosscheck the Gaussian logarithmic negativity near the transient-entangled regime.

The exact proof is given in `RESULT.md`; the finite truncation is corroboration, not a proof for the infinite-dimensional bosonic system. The script does not independently settle scientific priority or inspect inaccessible supplementary literature. The asymptotic bound asserts the existence of a finite eventual separable time rather than a uniquely determined first death time.
