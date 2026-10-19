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

# Verification record

The included `verify.py` was executed as a standalone Python 3 program using only the standard library and exact integer arithmetic. It returned `VERIFY_OK` after exhaustively checking 64, 729, 4,096, and 15,625 three-hole schedules for alphabet sizes \(2,3,4,5\) respectively; each was checked against the derived trace, exterior-square coefficient, one-cycle count, and exact class-frequency formula. It also reproduced both explicit binary matrices and checked the unipotent count law through thirteen positive horizons. The general mathematical conclusion rests on the proof in `RESULT.md`, not on this finite check.

The exact operations use no floating-point approximations. Independently replay with `python3 verify.py` after extracting the files embedded in the package. Endpoints of digit cylinders have zero Lebesgue measure and do not affect the stated probability identities. A separate independent mathematical audit has not been carried out.
