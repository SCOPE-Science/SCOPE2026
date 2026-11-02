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

# Reproducibility and limits
Run `python verify.py` with Python 3, mpmath and scipy available. The script checks the limiting Fourier-Parseval constants against direct Hurwitz-zeta quadrature at two exponents, evaluates finite-grid antithetic variance approaching those constants, and probes the endpoint singularity scaling for three exponents and three grid counts. The actual observed result was:

`VERIFY_OK: hurwitz_parseval=4, paired_grid_asymptotics=2, local_moments=9`

Analytic verification independent of finite sampling is laid out in the four proof steps in `RESULT.md`. The moment boundary is an infinite-domain integral-divergence argument and is not inferred from a Monte Carlo simulation. The uniform-in-coupling limiting optimality relies on Cauchy--Schwarz and L2 marginal convergence, not a finite search across couplings. The numerical tolerances are approximate tests, not independent validation.
