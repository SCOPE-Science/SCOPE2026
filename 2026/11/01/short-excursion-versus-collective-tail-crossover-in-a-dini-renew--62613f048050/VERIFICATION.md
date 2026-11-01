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

# Reproducibility
Run `python3 verification/check_pressure.py` with Python 3 and its standard library. The executed program completed 37 finite assertions, including an approximate location of the critical exponent, positivity/ordering checks on geometric-tail bounds for the pressure root at nine finite parameter pairs, and finite-entropy identities. The computed crossover is approximately 1.553201524280. Numerical pressure enclosures use floating-point arithmetic and Euler–Maclaurin zeta evaluation, not directed-rounding interval arithmetic. They cannot prove any infinite-limit claim.

The theorem is proved analytically in RESULT.md via exact renewal pressure, a uniform tail splitting with a polynomial cutoff, Laplace/Gamma asymptotics and monotonicity of a gamma expectation. No external or independent validation has been performed.
