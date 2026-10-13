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

The affine family and all displayed quantities are exact.

`artifacts/verify_inactive_scenario.py` verifies the branch structure, unique minimizer, exact optimal value, active-scenario descent, and inactive-scenario obstruction using symbolic and exact rational arithmetic.

The general model-decrement and norm inequalities are proved analytically from convex subgradient optimality in `RESULT.md`. The computation is supporting evidence only and is not used as an exhaustive proof.
