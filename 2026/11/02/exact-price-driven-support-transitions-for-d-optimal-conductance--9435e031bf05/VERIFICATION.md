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

Run `python verify.py` with Python 3 and installed NumPy and SciPy. The verifier constructs a 12-vertex cactus with three cycles (lengths 3, 4, 5) and two bridges. It performs 28 exact-rational grounded-cofactor versus cycle-product checks, 36 exact one-exception price-law checks (including equality), and 50 priced cactus optimizations with 900 asymmetric feasible comparisons. It also confirms local price budgets and the anticipated nonzero support. These are finite tests; the general theorem is established by proof. The weighted seven-vertex worked case additionally has a separately checked exact determinant of 27/98.

No independent audit is claimed or recorded.
