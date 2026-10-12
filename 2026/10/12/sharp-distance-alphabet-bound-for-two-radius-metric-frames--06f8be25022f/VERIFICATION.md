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

The mathematical proof is in `RESULT.md`. The provided pure-standard-library `reproduce.py` enumerates 5,042 admissible nested relation pairs on one through four vertices for nine second-threshold values with the first threshold normalized to one. It tests the triangle inequalities, exact strict relations, and claimed upper alphabet bound. It additionally checks the path lower-bound examples for each integer ratio floor from 2 through 9, and the three-point case for floor 1. Observed output begins `VERIFY_OK`. These finite experiments are supplementary and do not prove the statement over arbitrary sets or every real threshold ratio; that generality follows from the symbolic construction and reverse-triangle argument. No independent audit has been performed.
