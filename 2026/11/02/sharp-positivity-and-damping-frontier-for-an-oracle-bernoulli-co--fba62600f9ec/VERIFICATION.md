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

Run `python verify_cv_frontier.py` in a directory containing the supplied script. It has no dependencies outside the standard Python library, enumerates all sixteen Bernoulli outcomes and computes all sampled matrices and expectations using exact rational arithmetic. It explicitly tests parameter choices on both sides of the exact critical frontier and at equality.

The complete real-parameter proof is the positive-semidefinite matrix decomposition and the attained eigenvalue in `RESULT.md`. The executable tests are supporting checks of symbolic identities and do not certify an infinite family on their own. The verifier tests the *population-fixed* entrywise coefficients only, not coefficients estimated from data. Numerical implementation and full finite-element pipeline behavior were not tested. No independent audit has taken place.
