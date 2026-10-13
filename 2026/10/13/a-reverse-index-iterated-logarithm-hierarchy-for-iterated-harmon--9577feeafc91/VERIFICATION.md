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

Exact rational tests in `verify.py` regenerate the finite transposed-recurrence and base-case checks without relying on recorded logs. They verify 48 pairs, not the all-index asymptotic theorem. The unrestricted proof is the algebraic recurrence plus a fixed-endpoint induction using standard divergent iterated logarithm integrals. No outside validation or independent audit was performed.
