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

# Reproducibility and limits

Execute `python3 VERIFY.py` using a standard Python 3 interpreter. It enumerates all 5,461 input words of lengths zero through six over the alphabet `aAbB` (with `A` and `B` denoting formal inverses), and tests each conjugacy minimum against independently enumerated words of no greater length. The program prints `VERIFY_OK` and the counts recorded in RESULT.md. It checks 986 unrooted labelled tree shape classes and encounters 32 ordinary geodesics that are not conjugacy geodesics.

The general theorem is proved analytically by an indexed prefix/edge enumeration algorithm with deterministic logarithmic workspace. The verifier deliberately uses linear-space explicit Munn trees; it is **not** a performance or complexity certificate. Word equality in the free group is used as a known deterministic logarithmic-space primitive. No independent audit was performed.
