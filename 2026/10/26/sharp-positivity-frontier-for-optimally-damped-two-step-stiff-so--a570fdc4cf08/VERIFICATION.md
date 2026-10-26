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

# Reproduction and proof boundary

Run `python3 CHECK.py` with the standard Python library. It reports `CHECK_OK` only if exact-rational checks for the source coefficient reduction, all three characteristic identities, and finite representative positivity/sign-loss trajectories pass. The nonnegativity criterion for **all** integer iterates and **all** admissible parameters follows from the six steps of the analytical proof in RESULT.md and is not inferred from those finite checks. Strict positivity fails at the explicitly stated annihilation endpoint, which the theorem deliberately includes as nonnegative.

The source's optimality/A-stability statement is used only to identify the numerical-method family; the sign claims and all required identities are independently derived in RESULT.md. No claim of external or independent audit is made.
