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

# Verification of the stated stationary rate law

The standalone symbolic program `verification/check.py` reconstructs the generator from the original Itô equations and jump map, independently assembles the second- and fourth-degree moment linear systems, and checks exact formulas, derivative and asymptotic identities. It additionally tests four exact-rational choices of friction, trap stiffness, temperature and reset rate, with all stationary polynomial balance equations verified exactly.

Only algebraic identities and finite specializations are computationally checked. Existence and uniqueness of the invariant law, validity of the moment equations, and uniqueness of the positive optimizer rely on the complete analytical argument in `RESULT.md`. No independent external mathematical validation has been performed.
