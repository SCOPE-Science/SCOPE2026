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

# Verification and reproducibility

Run `python verify.py` with Python 3, NumPy and SciPy. The standalone program executed and reported `PASS 559 deterministic numerical and algebraic cross-checks` before this record was assembled. Its checks include independent exponentiation of the two-state telegraph characteristic generator, density-matrix pulse propagation, error bounds for Gaussian convolution, optimal peak phase scheduling, Fourier-factor limits and finite coupling/jitter tests.

The finite numerical checks corroborate intermediate exact formulas but cannot prove infinite-limit, optimization, or uniform-convergence assertions. Those are established by the explicit differential equations, uniform Lipschitz and Gaussian characteristic estimates, the location of the unique largest exponential-sinusoidal lobe, uniform Fourier convergence, and integration-by-parts bounds in `RESULT.md`. The terminal capacity is computed after ensemble mixing, and sign adaptation is allowed only when actual pulse time is known, not when the noise trajectory is known.

No independent review of the proof, priority, numerical program, or physical assumptions has been performed. The document makes no claim of finite-bandwidth feasibility or hardware work efficiency.
