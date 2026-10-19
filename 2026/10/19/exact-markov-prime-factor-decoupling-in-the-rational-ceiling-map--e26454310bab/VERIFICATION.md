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

Execute `python3 verify.py` using Python 3's standard library. The replay checks exact denominator-path probabilities for initial moduli `2,3,4,6,8,9,10,12,15` and horizons one through three, plus unit-polynomial bijections for moduli through 16 and two prime-power precision levels. The replay produced `VERIFY_OK`.

The general result for all starting denominators and finite horizons follows from the conditional unit-residue uniformity argument using Hensel lifting and induction, not from finite enumeration. Marginal hitting-time counts are credited to the 2012 primary paper. No independent or external audit has been performed.
