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
# Reproducibility

Run `python verify.py` with Python 3.10 or later. Its exact stdout is `replay.txt`. It evaluates the three-state recurrence independently on 27,000 triples and computes exact adaptive shattering ranks for the full two-hub graph with one through seven leaves. The proof of all orders is the induction in `RESULT.md`; finite brute force is not an infinite certificate. No independent scientific audit has been performed.
