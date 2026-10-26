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
The proof applies for all dimensions, all positive-definite real symmetric matrices and positive diagonal weights. The standalone `verify.py` uses exact rational arithmetic to check specific instances of each singular/negative Jacobian regime. The analytic argument uses the strict sine inequality, generalized Rayleigh principle, rank-one inertia bound, and regular-value degree formula. The tests are illustrations, not a substitute for universal proof. Independent audit was not performed.
