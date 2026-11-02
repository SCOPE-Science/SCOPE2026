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

# Reproducibility and scope
Run `python verify.py` with Python 3 and its standard library. The script uses exact rational arithmetic to check the SQP probe, the quadratic feasible optimum, the Hessian-induced normal reversal, the negative putative multiplier, feasible descent, and the objective gap across 16,269 rational parameter cases. It also exercises nine convex control cases. Observed output:

`PASS: 16269 nonconvex exact-rational witness cases; 9 convex control cases`

The proof in RESULT.md, not this finite checker, establishes the quantified statements for all real parameters and all positive-semidefinite quadratic corrections. No infinite computational enumeration, implementation-level convergence, or external audit is claimed.
