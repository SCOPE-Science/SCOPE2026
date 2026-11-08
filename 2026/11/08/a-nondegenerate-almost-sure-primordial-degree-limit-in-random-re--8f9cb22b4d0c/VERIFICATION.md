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

Run `python3 checker.py` with the standard Python 3 library. Observed: `PASS 3300 exact rational graph/transition assertions full shape enumeration through n=6, Markov chains through n=9`. It checks exact model mechanics and state recurrences. Finite checks are not a proof of the infinite almost-sure limit; see the separate conditional martingale and environment estimates in `RESULT.md`. No independent audit has been performed.
