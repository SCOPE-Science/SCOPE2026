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

The embedded `verification.py` uses only the Python standard library and exact fractions. It solves the four backward equations for the displayed rational example, checks both fixed-environment fixation probabilities, checks the sign of the threshold polynomial, and verifies the N=2 comparison at a rational parameter choice. These finite exact checks corroborate the example only; the parameter-wide result is proved by the backward-equation elimination in `RESULT.md`. No simulation is used, and no external certification or independent audit is claimed.
