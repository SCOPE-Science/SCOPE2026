---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The unchanged `verification/verify.py` uses graph neighborhood bit masks to check total domination and independence of the complement. It tests the explicit partition at selected vertices of maximum degree, and its exact small-graph routine visits all partitions via successive vertex insertion. It skips candidates with at most as many blocks as the current valid maximum; this is safe for computing the maximum. For the six-vertex boundary instance the maximum is three; the corrected result also proves this value directly.

The supplied `verification/verify_output.txt` records `VERIFY_OK`, with 72 eligible graphs among 33,864 labeled graphs of orders three to six, plus larger constructive or exhaustive checks and three small boundary cases. The additional positive-degree local case at maximum degree one is handled by the matching argument, not by this census. The finite tests are not a proof for unrestricted graph order.
