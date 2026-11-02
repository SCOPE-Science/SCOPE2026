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

The standard-library `verify.py` was executed on the scientific files accompanying this result. The observed output was `PASS: 536 exact-rational assertions`. All packet compositions of sizes \(2\le n\le12\), all conditioning packet counts, four rational cut probabilities and six rational moment parameter values were checked. The code uses exact rational arithmetic, not Monte Carlo.

The finite checker verifies claimed normalization, conditional equality and strictness cases, regression increments, and unconditional strict negativity on those instances. It does not substitute for the analytical proof of all-size claims or the renewal-reward central limit theorem. Independent mathematical audit has not been performed.
