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

# Verification notes
The published model and Hausdorff formula were read from arXiv:2610.31440v1 (22 October 2026), including its definitions (1.2)--(1.5), Theorem 1.1 and the explicit column-probability expression. Its source result is used as a premise, not reproduced or newly claimed.

The analytical checks are: (i) \(A-1\) allowable pair extensions at every history, (ii) at least \(\ell_b-1\ge1\) allowable extensions for each specified column, (iii) bounded-aspect rectangle counting, (iv) continuation-set bi-Lipschitz cylinders plus Baire category for packing dimension, and (v) strict concavity with a fixed sum of \(A-1\) surviving symbols.

`python3 check.py` reproduced the integer approximate-square count for eight seeded finite environments at all depths examined, and checked the strict-concavity equality cases on five integer count vectors. Result: `ALL_CHECKS_PASS`.

Finite enumeration does not establish asymptotics, infinite symbolic conjugacies or universal novelty. No independent audit was conducted. Limitations and competing literature are listed in RESULT.md and REVIEW.md.
