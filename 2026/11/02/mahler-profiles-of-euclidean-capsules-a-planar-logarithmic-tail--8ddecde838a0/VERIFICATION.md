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

# Verification evidence and limitations

The analytic proof in `RESULT.md` derives the polar integral, the strict monotonicity identity, the variance coefficient, the planar closed form, the higher-dimensional asymptotic integrals, and the half-normal limit. The reproducible checker `verification/check_capsules.py` was executed in a Python environment with SymPy and SciPy, returning the final line `ALL_CHECKS_PASSED`. It checks the exact three-dimensional identity, 13 low dimensions by independent numerical quadrature, a planar elementary closed form and its logarithmic expansion, five dimensions of the long-capsule second-order expansion, the dimension-400 Gaussian crossover and the dimension-1000 fixed-aspect convergence. Those numerical grids are limited and are not infinite proofs or independent review. The analytic derivations, rather than the checker alone, support the universal claims.

The user should not interpret the historical search as an exhaustive priority certification. The result does not claim noisy-estimator guarantees, dimension-uniform remainder estimates, or general cylindrical-family extremality.
