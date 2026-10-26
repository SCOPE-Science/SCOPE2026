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

# Verification of the finding

The analytical proof splits normalized two-level valuation matrices by the maximum cardinality of a matching through the valuation-one edges. For matching size three, perfect matching and unit normalized wages support the full core. For size two, two high edges and one low edge with the explicit lower worker wage support a factor of at least one-half of one plus the quality level. For size one, every high edge meets a single firm, and common normalized wage gives the exact lower factor; the grand coalition certifies the same upper factor.

Run `python3 verify_three_by_three.py` with a standard Python 3 interpreter. It exhausts 343 normalized incidence matrices, at five exact-rational quality levels, and verifies every coalition payoff inequality and EF1 without floating-point operations or third-party packages. The displayed expected success marker is `ALL EXACT CHECKS PASSED`. The finite tests do not prove the continuum result; that follows from the algebraic case split in RESULT.md. Independent audit or validation has not been performed.
