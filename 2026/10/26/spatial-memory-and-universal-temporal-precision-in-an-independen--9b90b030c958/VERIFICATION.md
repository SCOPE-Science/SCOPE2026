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
The submitted proof identifies and computes the integrated stationary indicator covariance for a single Brownian particle with its own Poisson resetting to a fixed anchor. Its point-process average then follows from the Campbell first-moment identity, without assuming anchor independence. Exponential domination justifies all interchanges and bounds the finite-observation-time remainder.

Run `python3 check_hyperuniform.py` from this directory. The reproducible output is embedded in `checker_output.txt`. The checker uses only Python's standard library and performs 25 independent exact-rational, numerical quadrature, and seeded probabilistic tests. These checks are limited to finite numerical cases and do not substitute for the analytic infinite-particle proof. Independent audit has not been performed.
