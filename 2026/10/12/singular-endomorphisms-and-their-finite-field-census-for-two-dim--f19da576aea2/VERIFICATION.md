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

Running `python3 verify.py` performs exact multiplication and homomorphism checks for each matrix and linear map over GF(2), GF(3), GF(4), GF(5), and GF(7). GF(4) is represented by a root of an irreducible quadratic over GF(2). The command prints counts and `VERIFY_OK` if all assertions hold. This is finite corroboration, not a substitute for the all-fields argument in RESULT.md. The argument classifies all singular morphisms via rank and proves counts by double-counting quadratic-root incidences; the monomial automorphism contribution is separately derived.
