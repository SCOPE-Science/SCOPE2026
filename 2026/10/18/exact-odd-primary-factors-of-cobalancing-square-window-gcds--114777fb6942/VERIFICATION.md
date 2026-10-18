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

Run `python verify.py` with Python 3 standard library. The included program derives the first five exact sums of squared half-cobalancing terms, uses their fifth-order recurrence reduction, and compares each odd gcd part for every length from 1 to 750 with independent order calculations for prime factors of the window length. The executed result was `PASS oddpart for 750 lengths`. The displayed selected samples agree. The proof of all positive lengths is contained in `RESULT.md`; finite tests alone would not suffice. No independent audit was performed.
