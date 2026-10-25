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

Run `python verify.py` with a standard Python 3 installation. No external packages, datasets, or network connections are required. The checker's exact rational tests exercise one-particle stationary second and fourth moments, two-particle mixed moments, stationary pair characteristic-function equations, finite-system variance identities, and perpetuity cumulants. Floating-point checks test finite geometric sums; a fixed-seed Monte Carlo check is restricted to the finite approximation of a known weighted-exponential representation.

Observed output: `PASS 99 exact and numerical checks; Monte Carlo mean=1.0020, variance=0.1457`.

The infinite series, its Laplace product, almost-sure geometric-kernel moment limits, conditional Lyapunov limit, weighted-exponential central limit, and the final triangular-array crossover are proved in `RESULT.md`. Neither finite arithmetic nor simulated samples are offered as proof of asymptotic convergence or historical originality.
