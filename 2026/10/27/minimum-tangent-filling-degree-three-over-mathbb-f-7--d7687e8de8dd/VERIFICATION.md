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

# Reproducible checks

Run `python3 verify.py` with standard Python 3. This checks exactly the 57 canonical representatives of projective-plane points over the seven-element field, identifies the 12 rational curve points and their gradient tangent lines, verifies their equality with the Fermat arrangement and their complete coverage, and counts tangency-line multiplicities (36, 9, 9, 3) at multiplicities (1, 2, 3, 5). A completed run returned `VERIFY_OK`. The proof of geometric smoothness and the conic lower bound are explicit symbolic arguments in `RESULT.md`; finite enumeration does not substitute for these geometric statements. Independent validation and independent audit have not been performed.
