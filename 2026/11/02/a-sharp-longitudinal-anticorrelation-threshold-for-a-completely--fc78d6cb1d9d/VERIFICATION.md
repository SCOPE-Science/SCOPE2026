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

The accompanying `check.py` is standalone apart from Python 3 and NumPy. It passed: 90 exact-rational moment identities and cubic-numerator tests; three exact rational sign checks for a reentrant parameter choice; four resonant crossing examples; two nonresonant crossing examples; positive transverse-lag tests; and independent stationary reset-age Monte Carlo comparisons at two parameter choices. The complete algebraic sign proof is in RESULT.md; finite simulations and floating-point tests are not infinite proofs.

Exact stationary-age sampling restarts the particle at the prescribed reset state, evolves Brownian orientation and harmonic propulsion over an exponential age, and estimates the mixed stationary moment without using the closed covariance formula in the sampler. Its time stepping is approximate; it is only a diagnostic.

No independent audit is represented by these checks. No claims are made for finite-sample detectability of exponentially small negative covariances or generalization beyond the stated reset protocol.
