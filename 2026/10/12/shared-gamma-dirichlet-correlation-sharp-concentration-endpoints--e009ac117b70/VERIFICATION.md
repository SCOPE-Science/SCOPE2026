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

The exact identities in `verify.py` use symbolic algebra to check the Beta second-moment normalization and the correlation-gap transformation, followed by reproducible seeded independent-Gamma numerical diagnostics. Directly simulated Gamma vectors check that their cross-covariance agrees with the common scalar multiple of the Dirichlet covariance matrix. A documented equal-margin calibration example is reproduced to sampling tolerance.

Numerical tests used explicit seeds and finite tolerances and ran successfully on the companion checker script. They do **not** certify the universal strict inequality or the limits. The finite-to-infinite inference relies instead on the analytic proof in `RESULT.md`: conditional independence and Beta moments, Gamma tail estimates, exponential-race convergence, and weak convergence of low-concentration Dirichlet vectors to simplex vertices. No independent audit or external validation has been performed.
