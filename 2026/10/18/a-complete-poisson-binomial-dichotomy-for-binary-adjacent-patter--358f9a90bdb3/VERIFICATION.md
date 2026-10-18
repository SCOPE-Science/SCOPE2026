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

# Reproducible scientific checks

Run `python verify.py` using Python's standard library. The program explicitly enumerates all binary sequences through length ten at four rational biases, computes each of the four pattern-count distributions by exact rational arithmetic, and compares the predicted oriented-pattern generating polynomial with those exact probabilities. It checks the two or three leading equal-word coefficients and the strict Newton inequalities at the relevant lengths. It also checks the explicit cosine-factor product numerically. The last check is numerical; all polynomial distribution and inequality checks are exact rational arithmetic.

The infinite-parameter claim relies on the matrix recurrence, a polynomial identity for Chebyshev \(U_n\), and the explicit strict Newton contradiction; finite computation is not a substitute for any of those steps. The primary-source and novelty comparison is limited to the specific inspected material reported in REVIEW.md; the relevant Martin full article was not read. Independent assessment has not been performed.
