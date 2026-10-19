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

The proof derives all-length reversal exclusion from substitution block boundaries. The Python 3 checker (`python3 check_factors.py`) independently tests the stated finite parameter grids and prints `VERIFY_OK`. For bases at least three, the checker constructs four-letter factors from the complete substitution pair closure; for base two it uses a finite generated prefix. Neither finite test replaces the infinite proof. All operations are exact integer and tuple operations; no probabilistic tests are used.
