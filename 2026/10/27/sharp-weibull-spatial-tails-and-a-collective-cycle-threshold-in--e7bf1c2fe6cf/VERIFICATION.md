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

The complete source `check_tail.py` runs with Python, NumPy, and SciPy and verifies 86 deterministic numerical and algebraic assertions for independent coefficient expressions, optimized finite-history costs, explicit Rayleigh moment-generating functions, and stationary second moments. It was executed successfully after extracting the final code from the package. This program is a finite numerical consistency checker, not an infinite-tail proof or independent scientific audit.

The stationary off-age distribution, the geometric backward history, and the Gaussian scale mixing are proved analytically in `RESULT.md`. The almost-sure convergent perpetuity and the variational asymptotics are infinite statements that finite simulations cannot establish. The cited sources provide the model framework and comparison literature. The present work does not supply a rigorous density prefactor or treat simultaneous parameter singularities.
