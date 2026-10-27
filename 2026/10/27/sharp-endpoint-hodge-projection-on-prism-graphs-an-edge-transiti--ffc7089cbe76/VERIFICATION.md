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

The exact-rational checker `verify_prism.py` was executed with Python 3 and SymPy and passed 539 assertions. It reconstructs graph incidence matrices, verifies the projection and the row-sum formulas for 3 through 12 rungs, and checks the phase expansion numerically at six larger sizes. Finite tests are not an exhaustive proof of the all-size formulas or the oscillatory limit; those rely on the displayed Green-function and cutoff arguments in RESULT.md. The prism-resistance literature comparison has an explicitly stated full-text access limitation.
