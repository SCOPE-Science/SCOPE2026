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
Run `python3 verify.py` from this package. The program tests all moduli `3..400` by independently enumerating the powers of each coprime residue until the orbit repeats and comparing the exact count to the factorization formula. The result is `VERIFY_OK` with 398 comparisons. This is finite verification, not a substitute for the general proof in `RESULT.md`.
