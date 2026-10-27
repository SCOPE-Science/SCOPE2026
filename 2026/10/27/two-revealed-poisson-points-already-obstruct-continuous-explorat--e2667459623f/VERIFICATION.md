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

# Verification notes

Run `python3 check_result.py` from the same directory. The exact finite script checks all eight occupancy patterns, their cylinder implications, the at-most-two occupied selected prefixes and the two witness configurations used to force contradictory exploration. It also tests first-point-prefix consistency on a 64-configuration finite simple model.

The actual script was executed and passed. The analytic claim needs the full proof given in RESULT.md: its key input is intensity-continuous increase starting from the empty Poisson configuration, and the positive probability of configurations avoiding the first explored region. Enumeration does not establish continuity or universal nonattainability.

Self-review: passed. Independent audit: not yet performed.
