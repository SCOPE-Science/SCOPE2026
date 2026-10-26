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

# Reproduction

Run `python3 verify.py` with Python 3 and the standard library. It terminates on any discrepancy. The replay checks 265 independently computed direct first-zero modular Fibonacci ranks, 163,840 exponent-state orbits, and the least smooth inputs at heights 5 through 8. The checks cover finite cases and support the stated recurrence; the universal statements are proved in RESULT.md.

Same mathematical model proof reconstruction and source comparisons have been performed. An independent audit has not been performed.
