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
Run `python3 verify_arch_run_joint.py` with Python 3 standard library only. The script checks every binary word through length 17 against the exact coefficient law, uses the defining all-subsequences test independently through length 11, and verifies the support constraints. Expected concluding line: `VERIFY_OK: definition through n=11, full joint coefficient enumeration through n=17`.

These finite tests do not prove the all-length claim; the formal-state equations and exact coefficient extraction in RESULT.md do so. The suite does not claim external or independent certification.
