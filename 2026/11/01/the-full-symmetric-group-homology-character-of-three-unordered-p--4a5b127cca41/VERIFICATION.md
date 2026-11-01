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

The standalone script `verify_petersen_three.py` uses Python's standard library. Executing `python3 verify_petersen_three.py` yields exactly `verification_output.txt` and ends with `VERIFY_OK`. It checks the chain dimensions, degree-one through degree-three boundary compositions, prime-field ranks, spanning by graph five-cycles, signed and orbit-formula Lefschetz traces for all seven conjugacy classes, and the complete Specht decomposition via exact Murnaghan–Nakayama recursion. Prime-field ranks serve only as lower bounds on rational ranks; the proof supplies the necessary upper bounds. No integral torsion, publication-priority uniqueness, or external independent audit is certified.
