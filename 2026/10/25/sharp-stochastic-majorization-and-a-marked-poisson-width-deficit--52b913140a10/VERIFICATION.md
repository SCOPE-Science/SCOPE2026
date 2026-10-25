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

# Verification

The accompanying `verify.py` uses only the Python standard library and can be run in the extracted package directory with `python3 verify.py`. It enumerates color allocations and directly optimizes complete-multipartite Gaussian support for small profiles, comparing the exact conditional extreme-cap survival law; separately it checks 5,352 outward unit transfers, integrates the predicted limiting tail against the closed constant, and runs a seeded Gaussian event-frequency sanity check. Actual observed output: `VERIFY_OK exact_conditional_cases=33 transfer_cases=5352 montecarlo=6000 positive_fraction=0.27350 expected=0.26667`.

The proof of the infinite-dimensional Poisson limit, uniform integrability and stochastic extremality is analytical in `RESULT.md`, not inferred from these finite tests. Bounds for standardized Gaussian maxima and classical Poisson convergence are mathematical inputs. The role of the numerical checks is corroborative only.
