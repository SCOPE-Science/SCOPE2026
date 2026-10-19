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

## Checks

The included `verify.py` requires only Python 3 standard library and tests the original finite-rate passive propagator against the published mean-square law at exact rational inputs, limit Gaussian-mixture factorial moments, high-rate second-moment asymptotics, sample stationary reset excursions, and the pointwise exponential-kernel error inequality. Direct execution of the complete embedded program is required for its assertion count. The infinite-law convergence is analytical and cannot be established by the finite tests.

## Scope

The exact \(W_2\) estimate is proved for the fixed-reset-orientation complete-reset inertial active Brownian model at fixed inertia. Possible implicit broader-theorem coverage remains an originality risk. Independent audit has not been performed.
