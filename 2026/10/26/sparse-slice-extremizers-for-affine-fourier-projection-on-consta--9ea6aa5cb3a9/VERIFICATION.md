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

# Verification and reproducibility

Run `python3 check_eventual_width.py`. The new finite checker compares the exact optimizer prediction with the full hypergeometric absolute row sum at all smaller widths for 143 sample sizes, and checks the strict signs on both sides of 48 predicted transitions. The proof of eventual localization and the exact arithmetic threshold are in `RESULT.md`. The finite checks do not establish an earliest cutoff or replace that proof. The original kernel checker, `johnson_projection_check.py`, pertains to the exact row norm and does not check the new eventual-width statement.
