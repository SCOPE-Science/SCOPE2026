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

# Verification notes

Run `python verify.py` using only the Python 3 standard library. In the recorded execution, the script returned:

`VERIFY_OK: nodal_and_moment_checks=2288, K=0..3, N=31,47,79,127, negative_mass_cases=12, Dirichlet_slopes=0.2023985,0.2025084, target=0.2026424`

The checks construct the positive quadrature weights for explicit Fourier grids, verify first Fourier moments and all grid cardinal values, and compare numerically integrated off-grid negative mass to the theoretical upper bound. The convergence of the high-degree Dirichlet negative-mass increment is checked only as a numerical diagnostic. Positive-analytic Poisson mixtures and metric-projection continuity are proved in RESULT.md; the finite numerical tests are not used as evidence for an infinite theorem.

Limitations of verification: floating-point linear solves and trapezoidal numerical integration can have roundoff errors; no exhaustive exact-arithmetic or independent review was conducted. The entire analytic proof must be assessed directly for independent validation.
