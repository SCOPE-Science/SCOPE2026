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

# Reproducibility checks

Execute `python3 VERIFY.py` using Python 3 and its standard library. The script calculates the exact thirteenth companion matrix, the three trace slopes, lifts the unique roots through fifteen ternary digits, and independently compares the formula against 119,998 terms of the defining recurrence. It checks the discrepancy bound at all 119,998 corresponding cutoffs for twelve valuation levels. The observed program result was `VERIFY_OK matrix=13 slopes=3 hensel_roots=3 lift_depth=15 recurrence_indices=119998 discrepancy_cutoffs=119998 root_mod_6561=(4477, 2107)`.

The analytical proof establishes all indices and valuation levels without relying on a finite search. Exhaustive finite tests do not certify novelty or replace the argument. Independent mathematical audit was not performed.
