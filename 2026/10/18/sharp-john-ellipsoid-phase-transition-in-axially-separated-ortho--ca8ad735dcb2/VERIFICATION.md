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

# Computational checks and limits

The standalone file `verify_exact.py` was executed successfully, returning:

`VERIFY_OK exact_cases=8 sampled_directions=110000 contact_cases=11`

Checks include exact rational identities for eight separation parameters, exact algebraic values at the phase transition, the reduced support-boundary equalities, random-direction support containment for eleven configurations, and active-direction tangency. The random-direction tests cover a finite sample only and are explicitly **not** the proof that containment holds for all directions; the analytic minimax argument in `RESULT.md` supplies that universal step. The global volume-optimality argument uses classical John-ellipsoid uniqueness and strict scalar differentiation, not a numerical solver. No external validation was requested or performed.
