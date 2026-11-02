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

# Verification and boundaries

Run `python3 verify.py` from this package directory (Python standard library). It passed `260` deterministic exact-rational/numerical assertions. The exact checks independently compare stationary-generator and GEM fourth moments, the two-dimensional beta special case, and finite-dimensional variances; numerical tests check genuine sphere directions in dimensions 2, 12 and 64, a fixed-weight conditional central-limit variance, and the max-weight rare-event squeeze. The code is not an infinite-proof certificate.

Proof dependencies: the Poisson stationary backward representation, beta-function stick recursion, covariance of independently uniform sphere directions, multivariate CLT with truncation controlled in conditional L², and the size-biased GEM measure identity (proved by Hausdorff moment uniqueness). See RESULT.md, Steps 1–5. Finite samples cannot prove the limiting Gaussian-mixture law, the endpoint coefficient or independent novelty.

The exact stationary Dirichlet-process construction and published low-dimensional densities are credited to Guéneau, Majumdar and Schehr (2026). No thermal noise, anisotropic propulsion, or simultaneous dimension/persistence scaling is asserted.
