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

# Verification of the parity–leaf covariance identity

Run `python verify_parity_leaf.py` with Python 3 standard library. The checker enumerates every rooted ordered tree with \(2\le n\le11\) vertices and makes 113 exact assertions comparing Catalan totals, both Narayana marginal histograms, rational means, variances, mixed moments, covariance, correlation and the mixed-derivative coefficient. Expected console message: `PASS 113 exact assertions; exhaustive plane trees n=2..11`. The checker uses integer counting and `fractions.Fraction`, not floating-point numerical approximation.

Unbounded-size correctness follows from the two-type functional equations, formal implicit differentiation, and binomial coefficient extraction reproduced in RESULT.md. Exhaustive enumeration through eleven vertices is not an exhaustive proof of that unrestricted statement. Earlier similar enumerative work, especially the inaccessible full text of Mallows and Wachter (1972), remains a historical-priority limitation. No external independent audit has been performed.
