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

The standalone `verify.py` program runs on Python 3 without packages. Execute `python3 verify.py` from the directory containing this file. The output `VERIFY_OK` confirms the exact Jacobian-ring character multiplicities `(0, 70, 290, 70, 0)`, the coarse Euler count `435`, and the commuting-pair Euler count `441`.

The program checks finite arithmetic and numerical consequences; the proof of exhaustive fixed-sector geometry, normal weights and the age shift is given in `RESULT.md`. Finite arithmetic is not substituted for the geometric proof. The identity of the non-symplectic diagonal generator matters: a different symplectic diagonal subgroup can have the same pair of invariant Betti multiplicities without yielding this orbifold profile. No independent audit or validation has been performed.
