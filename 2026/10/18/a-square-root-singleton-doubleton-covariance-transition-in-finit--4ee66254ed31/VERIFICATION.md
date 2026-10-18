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

The attached standalone `check.py` uses Python exact fractions to enumerate all Dirichlet-multinomial occupancy count vectors and independently compare their singleton–doubleton covariance with the factorial-moment formula. Checked 72 combinations: 3 population sizes, 6 sample sizes, and 4 rational per-species concentrations. All matched exactly. High-precision gamma-function evaluation checked 9 continuous roots for three fixed total concentrations and three population sizes, including opposite signs on either side of the predicted offset; all passed.

The proof is analytic. Enumeration does not certify a statement about arbitrarily many species or arbitrarily large samples. The claimed global sign classification is restricted to sufficiently large populations with fixed total concentration below one. The gamma-continuation root is a comparison threshold, not a realizable noninteger sample size. Independent audit has not been performed.
