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

# Reproducibility and verification
The accompanying `verify_ultraold.py` runs exact rational enumeration of all parent-choice trees with six vertices for three negative integer exponents and compares the finite-tree variance with the innovation recurrence. It also performs seven numerical checks for strongly negative exponents, using a finite truncation to inspect the three-scale asymptotic. All ten assertions passed in the recorded run.

The analytic proof's bounds on the omitted infinite tail, stated in `RESULT.md`, are essential. No finite enumeration establishes the infinite asymptotic. No independent audit or external validation is claimed.
