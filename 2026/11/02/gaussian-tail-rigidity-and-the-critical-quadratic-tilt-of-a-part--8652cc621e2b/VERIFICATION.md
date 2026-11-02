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

Execute `python3 verify.py` with Python 3.10 or later; no third-party packages are required. A successful check emits `PASS: 54 bounded numerical / rational checks; all asymptotic claims require proof.` The checks include independently implemented exact rational generator-moment identities, Gamma/product comparison for large indices, seeded Poisson-age variance perpetuity sampling, quadrature of the complete-reset mixture density, and the borderline Beta-factor identity. The seeded runs use bounded sample counts; Monte Carlo tolerances are explicit in the code.

The proof of the exact stationary law, its asymptotic density equivalent and the quadratic exponential moment boundary is mathematical, not experimental. It uses stationary backward stochastic integration, conditioning on independent Poisson ages, a convergent infinite product, and dominated convergence. Bounded numerical checks do not establish statements involving all parameters, arbitrarily large moment indices, or infinite spatial limits.

The largest novelty uncertainty is the possibility of an existing general Gaussian variance-mixture/perpetuity edge theorem implying the specialized constant. Closest primary literature concerns either the diffusion approximation, the second moment of a related harmonic model, unconfined proportional resetting, or resetting to an independent distribution.
