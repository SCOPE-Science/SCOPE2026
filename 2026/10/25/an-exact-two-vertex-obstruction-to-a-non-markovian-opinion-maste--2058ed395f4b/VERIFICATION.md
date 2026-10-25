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

# Reproducibility

Execute `python verify.py` with Python 3.9 or newer from this package. The checker uses exact integer/fraction arithmetic to establish an explicit polynomial antiderivative for the positive discrepancy integral and its exact series coefficient, and checks a separate first-event probability partition for both heterogeneous and homogeneous example probabilities. The mathematical proof supplies the stochastic first-ring argument and the renewal-density formula for the entire interval. No random sampling is used, and no infinite conclusion is inferred from finite tests.

The original article's stochastic interpretation and the exact integral identity have been checked against the accessible primary PDF, pages 2626–2628. The demonstration is a counterexample to asserted *exact marginal closure*, not a criticism of the renewal integral equation as a separately defined deterministic dynamical system.
