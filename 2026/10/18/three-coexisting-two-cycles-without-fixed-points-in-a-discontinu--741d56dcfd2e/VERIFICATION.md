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
The self-contained `verify.py` checks all four exact alternating-sign evaluations using 65-digit Decimal arithmetic, verifies the rational squared inequality with Fraction arithmetic, bisects one scalar root in each of the three certified disjoint intervals, evaluates all three two-step multipliers, checks the inverse-branch cycle relations, and verifies the exact numerical coefficient in the right fixed-point bound. The analytic proof in `RESULT.md` establishes that these are the **only** cycles for exponent different from one and proves the boundary conventions; no finite script is treated as an infinite-state certificate.

Independent mathematical audit has not been performed. Originality is assessed relative to the inspected original publication, published neighboring hypotheses and real database queries; unindexed equivalent antecedents remain possible.
