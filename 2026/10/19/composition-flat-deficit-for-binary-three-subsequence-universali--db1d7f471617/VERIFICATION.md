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

The proof is symbolic. Its critical steps are the equivalence of three-subsequence universality and at least three complete-alphabet greedy arches, uniqueness of arch factorization, and a coefficient difference of two rational bivariate series.

The standalone script `check_fixed_weight_3univ.py` independently determines universality by direct matching against all eight binary length-three targets. Its actual successful execution covered every word through length sixteen: 131071 words and 153 parameter pairs. It checks the closed form at every composition and the boundary cases.

The finite computation is not a proof for unbounded word length; that role belongs to the formal coefficient argument in RESULT.md. No separate external validation has been performed.
