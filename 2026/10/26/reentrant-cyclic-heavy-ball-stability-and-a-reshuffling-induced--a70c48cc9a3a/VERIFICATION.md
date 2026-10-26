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

The supplied `verify.py` uses exact rational matrix multiplication and checks both frozen-order propagators, their characteristic roots through trace/determinant, and a positive-definite lower bound for the average quadratic amplification under independent epoch permutations. It separately evaluates 1536 additional rational trace and determinant cases. The analytical proof in RESULT.md provides the all-parameter claims by the quadratic Schur criterion and the elementary geometry of a convex quadratic; the finite checks are diagnostic only. The quantified divergence concerns mean-square state norm and does not certify almost-sure divergence. The source comparisons and independent novelty validation remain open to external review.
