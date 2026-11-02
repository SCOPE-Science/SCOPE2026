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

# Checks and boundaries

The analytic calculation uses exact rational Dirichlet monomial integrals, controlled sine remainders and elementary quadratic covariance identities. The embedded `verify.py` performs exact factorial-moment and coefficient checks in rational arithmetic. Running `python3 verify.py --simulation` also produces random-gap corroboration, equivalent to random uniform circle endpoints. Simulations and finite samples are not an infinite-dimensional proof. The finite-sample optimality is a variance statement, not minimum mean squared error; prior leading extrapolation formulas are cited explicitly. Independent audit: not performed.
