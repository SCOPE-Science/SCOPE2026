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

# Reproducibility and limits

`python verify.py` enumerates attachment choices to order nine with exact `fractions.Fraction` probabilities and independently checks the marked root degree, whole-tree leaf count, exact mixed covariance, marked leaf probability, and second root-degree moment. Exact finite differences are separately checked to order 249. Floating-point numerical comparisons at orders 1000, 10000 and 100000 are diagnostics only.

The proof for all integers \(n\ge2\) follows from the conditional-product identity, the central-binomial formula and a telescoping variance recurrence in `RESULT.md`; no program is presented as an infinite-dimensional certificate. The self-review is recorded in `REVIEW.md` and `AUDIT.json`. Historical-priority verification remains subject to independent assessment.
