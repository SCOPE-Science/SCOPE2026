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

# Reproducing the calculation

From a directory containing `verify.py`, execute `python3 verify.py` with Python 3.8 or later. A successful execution prints `VERIFY_OK`, verifies the sixteen integer transfer entries, checks the five rational values, and independently enumerates all residue classes for the sixteen finite representatives.

The theorem's infinite reach comes from the proved zero-gap saturation argument: any carry persisting across three zero bits is incompatible with at most three carries. Finite enumeration alone does not establish that reduction. The transfer recurrence and the exact integer count table are spelled out in `RESULT.md`.

No random sampling or floating-point computation is used. A further 169-pair bounded parameter check is included as a consistency test, not as a substitute for the proof. No independent external audit has been performed.
