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

# Checks and scope

The Riccati equation was reconstructed from the modified Bessel recurrence and derivative identities. Strict order log-convexity yields dimensional ordering. The upper and lower root brackets follow at the unique level-two crossing. The Gamma expectation representation was checked against Bessel integral normalization; standardized Gamma moments and sixth-order Taylor remainders yield a uniform order-two expansion. The exact correction is a consequence of the analytic proof, not of numerical extrapolation.

The included `check.py` and `check_output.txt` record independent symbolic algebra paths and numerical checks at ten integer dimensions. The numerical sample does not establish a claim for untested dimensions.

Primary reference: Evans–Majumdar 2014, arXiv:1404.4574v1, equations (65)–(77). Supplementary mathematics: Segura 2021, arXiv:2105.02524, Bessel-ratio Riccati estimates.

The result concerns the coefficient after the small-target asymptotic is taken at each fixed dimension; finite-size and uniform double limits are not covered. Any independent validation is pending.
