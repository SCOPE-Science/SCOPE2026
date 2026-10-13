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

Run the included exact-arithmetic checker with `python checker.py` (Python 3 standard library). The checker builds the count transition kernel independently of the stationary-factorial recurrence, solves the stationary linear equations over rational numbers and verifies all stationary inclusion probabilities, full-state flux and pairwise covariance at sizes 2 through 8 and at four survival probabilities. Output: `PASS exact finite stationary identities: 280 assertions`.

The stationary factorial-moment recursion, generating-polynomial inversion, critical-loss logarithmic Riemann sum and strict derivative inequality are analytic arguments in `RESULT.md` and hold for the stated infinite domains. The finite exact calculations do not imply the infinite-domain claims by themselves. No independent audit has been performed.
