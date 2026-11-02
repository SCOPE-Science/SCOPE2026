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

The accompanying `verify.py` uses only the Python standard library. Execute `python3 verify.py` to reproduce the displayed deterministic checks. It implements the centered stationary polynomial generator and, independently, numerical quadrature of the Poisson-integral fourth cumulant. It also evaluates both temporal orders of mixed moments using the independent transition innovation, checks the analytic maximizer, and evaluates finite-order mixed-cumulant coefficient identities.

Test families include a symmetric four-point mark distribution, an asymmetric two-point distribution with nonzero raw third moment, and deterministic positive marks. Thermal diffusivity is varied independently from zero to positive values. Tests verify invariance of the fourth-order witness across three thermal-noise strengths when the kick process is fixed.

Analytical validity rests on independent increments, moment–cumulant identities, existence of the stationary stochastic convolution under finite fourth moment, and elementary maximization of a cubic factor. Numerical quadrature and finite test cases do not establish the infinite parameter-domain result by themselves. The tests do not measure finite-sample estimation error or entropy production. Independent external validation has not been performed.
