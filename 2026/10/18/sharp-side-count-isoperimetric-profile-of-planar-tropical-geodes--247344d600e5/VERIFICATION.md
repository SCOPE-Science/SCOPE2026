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

# Reproducibility and scope

The polynomial identities and rational polygon tests were executed from the packaged file `tropical_profile_checker.py` with Python 3 and SymPy; they returned `VERIFY_OK: 4103 exact polygon cases and 3 symbolic identities`. The checker directly computes tropical length, shoelace area and exact rational equalities, rather than asserting them from theorems under test.

The infinite statements rest on the analytic classification and the displayed exact sum-of-squares expressions in RESULT.md. The six-sided inequality and equality case use the cited primary literature. A finite number of tests cannot independently establish the general classification or scientific originality. Independent scientific audit has not been performed.
