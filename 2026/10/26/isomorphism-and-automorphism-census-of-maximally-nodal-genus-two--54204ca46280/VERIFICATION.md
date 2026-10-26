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

The complete proof and all hypotheses are in `RESULT.md`. Run `python verify.py` from the directory containing this file and `verify.py`; the checker prints `ALL_ORBIT_CHECKS_PASSED` after testing representative torsion actions and automorphism orders. These finite checks do not establish a theorem for arbitrary prime powers. The universal argument is the Frobenius torsion exact sequence, normalization functoriality, and finite group fixed-point enumeration in `RESULT.md`.

The source's original nodal construction and the older maximal point bound have been compared at their mathematical statement level. No independent expert review or machine proof exists for this result.
