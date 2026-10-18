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

# Reproducible checks
Run `python3 verify_coupon.py` using Python 3 standard library. Its exhaustive word calculations directly test the stopping definition on bounded instances; its separate exponential-generating-function calculation tests the exact coefficient law; exact rational cross products test the claimed strict likelihood-ratio order across adjacent feasible times and parameters, including zero and positive null weights. The script prints its check counts. No exhaustive finite computation proves the all-parameter statement; the proof is in RESULT.md.
