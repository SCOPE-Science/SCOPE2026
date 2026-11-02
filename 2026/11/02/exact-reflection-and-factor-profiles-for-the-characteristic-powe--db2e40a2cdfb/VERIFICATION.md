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

# Verification and scope

The executable `verify.py` independently generates powers-of-two indicator prefixes, enumerates their distinct factors and the equivalence classes under reversal, and compares them with the exact formulas. It tested 194 lengths in each of the two one-sided boundary conventions (388 checks in total), including lengths through 180 and dyadic-boundary cases through 1025. It also checked the gap-count identity at 65,533 consecutive lengths. The executable returned `VERIFY_OK` without exceptions.

This is finite computational corroboration only; the infinite claim is established by the complete gap classification in `RESULT.md`. The source distinctions and scientific priority limitations are documented in `REVIEW.md`. No external independent audit has been performed.
