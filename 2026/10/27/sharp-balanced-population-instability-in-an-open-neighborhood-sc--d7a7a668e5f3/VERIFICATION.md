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

The exact `verify.py` enumerates all colorings for \(2\le n\le6\), tests every red–blue pair by relocating both agents before recomputing their original-color utilities, and agrees with the finite specializations of the theorem. The infinite conclusion follows from the two strict-product inequalities proved in RESULT.md, not from the enumeration. No formal proof assistant or independent audit was used.
