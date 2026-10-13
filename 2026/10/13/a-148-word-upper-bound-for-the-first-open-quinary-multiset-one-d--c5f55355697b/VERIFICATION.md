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

With the embedded `verify.py`, run `python3 verify.py`. The program performs complete finite integer-arithmetic checks of all 715 cover constraints, all 495 weighted shadow vertices, all 23 input types, the 18 shadow types, and the explicit 143-word disjoint-shadow construction. Each assertion is a necessary step in the finite certificate. No solver outputs, logs, or external data files are trusted. This verifies the upper and lower bounds but cannot assert a stronger upper bound or exact maximum. Independent audit: not performed.
