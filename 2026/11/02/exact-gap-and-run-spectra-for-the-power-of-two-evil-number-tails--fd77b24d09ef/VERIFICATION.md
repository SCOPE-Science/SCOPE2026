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

Run `python3 verify_evil_tail.py` with a standard Python 3 interpreter. The program constructs every evil generator up to the finite test limit, applies a reachability calculation for the generated additive monoid, and compares every absent integer and its consecutive run structure against the exact formula. It checks all integer exponents from 2 to 10 inclusive and reports nine PASS results covering 6,132 gaps and 4,106 candidate generators. The checks cover a finite range only; the mathematical proof establishes all exponents and integers. No independent external validation has been performed.
