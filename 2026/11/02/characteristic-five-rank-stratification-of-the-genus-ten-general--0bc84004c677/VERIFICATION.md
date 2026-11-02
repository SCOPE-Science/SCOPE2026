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

The supplied `verify.py` was executed with Python 3 and standard-library only. Its exact finite-characteristic coefficient arithmetic expands the product of two cubics to the fourth power, builds the ten-by-ten Frobenius coefficient matrix and verifies all six nonzero entries and every zero entry. It prints the formal factors of three paired two-by-two blocks, checks that all three admissible base-field parameters give rank four, and terminates with `VERIFY_OK`. The symbolic identities (not those three finite tests) certify the classification over the algebraic closure. Smoothness, genus and the stable-rank-to-p-rank identification are demonstrated in `RESULT.md` and are not asserted solely on log evidence. Independent audit: not performed.
