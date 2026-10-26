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

The self-contained program `verify_friedman.py` uses `fractions.Fraction` for the killed chain and checks the exact recurrence, probability mass, and upward-transition bias for eighty successive times. The checked output is in `verification_output.txt`. This is finite verification, not a proof of a tail asymptotic; the infinite result is proved analytically in `RESULT.md`. No external audit or independent validation was performed.
