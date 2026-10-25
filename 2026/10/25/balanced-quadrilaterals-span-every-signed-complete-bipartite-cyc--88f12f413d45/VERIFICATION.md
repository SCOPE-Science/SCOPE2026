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

Run `python verify_signed_glmy.py` with Python 3 and SymPy. The script uses exact signed integer matrices, exhaustive switching-normalized sign patterns of six size pairs (606 total), and separately constructs all permitted backtracks and equal-endpoint two-step path relations for 94 smaller covers. It compares boundary ranks and proves that the computed degree-one quotient has zero dimension in these finite cases.

The mathematical proof in `RESULT.md`, not this finite experiment, establishes the all-parameter assertion. No independent human or external audit was performed. Full text of the 2026 signed GLMY preprint could not be accessed during the literature comparison.
