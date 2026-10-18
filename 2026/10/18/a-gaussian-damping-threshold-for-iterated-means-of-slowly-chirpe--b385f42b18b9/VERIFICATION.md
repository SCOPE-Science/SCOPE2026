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

# Reproducibility and analytical checks

The embedded `check.py` runs under Python 3 standard library without network access. In the packaged execution it reported `PASS: 387 independent finite numerical assertions`. It calculates centered binomial probabilities recursively, independently compares short direct binomial sums with the recursive implementation, checks the complex characteristic-function linearization at representative dimensions, and tests the amplitude regimes for selected parameters. No test is represented as a proof of a limit.

The mathematical proof verifies the operator-family hypotheses (positive bounded weights), an exact binomial iterate formula, a fixed-coordinate Taylor remainder of order \(O(n^{\beta-1})\), the binomial characteristic function, strict separation of the subcritical/critical/supercritical cases, phase subsequences, uniform norm identities, essential normality, and Cesàro averages. The fourth-order expansion is used only with relative error where its leading exponent diverges. Independent mathematical and bibliographic audits have not been performed.
