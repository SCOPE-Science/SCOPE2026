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

# Verification instructions and limits
Run `python3 checker.py` using standard Python 3. A successful result ends in `ALL_CHECKS_OK` and displays the complete strict-chain coefficient vector and small finite-valued counts. The checker considers all `4096` directed off-diagonal binary masks, checks reflexivity by fixed diagonal and all `64` ordered transitivity triples, enumerates the `355` preorders, and computes the exact strict-chain recurrence for lengths `1` through `9`. It independently counts two nested cuts for the three-level case and directly checks all three-world fuzzy matrices through five levels.

The certificate is finite and exhaustive for its stated four-world integer coefficients, not for arbitrary world counts. The polynomial equality is verified at ten integer points with an independently justified degree-nine bound. Independent audit was not performed.
