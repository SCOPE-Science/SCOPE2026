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

# Mathematical verification

The included `verify.py` recomputes the divisors' Euler-totient weights by exact integer arithmetic, forms every subset sum as a bitset and compares degree-completeness with the theorem on a finite parameter grid. It also independently computes maximal gaps to check the three exact cofactor formulas. The expected output is `VERIFY_OK three-prime_cases 64 cofactor_gap_cases 72`.

The proof itself is unbounded. The checker is corroborative and does not independently validate the infinite theorem. Published antecedents and priority limitations are identified in the review.
