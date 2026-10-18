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

# Verification

`verify_run_pause_reverse.py` executes independently reproducible symbolic and matrix-exponential computations. It checks the generator determinant, Laplace resolvent, trap real-mode amplitude, critical-boundary factorization, and 64 covariance points for eight parameter tuples including tuned cancellation and equal-decay conditions. Twelve further checks evaluate the tuned sinusoid away from its zeros. Total: 82 assertions passed.

The matrix-exponential calculation evolves a stationary position–forcing cross-covariance vector without using the closed filtered formula, and independently checks that formula over the stated samples. This cannot prove infinitely many strict crossings; the analytical spectral-dominance and factorization arguments do so. The theorem does not cover colored translation noise, nonexponential pauses, or arbitrary reset orientations.
