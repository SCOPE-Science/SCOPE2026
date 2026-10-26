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

# Reproducible calculation

Run `python3 check_fan.py` with Python 3 and its standard library. The checker builds every source-edge incidence vector, constructs the grounded graph Laplacian independently from incidence columns, solves each source equation by pivoted exact-rational Gaussian elimination, computes the absolute current sums and diagonal corrections, and compares the results with the displayed Fibonacci–Lucas formulas. It covers the 21 graphs with \(2\le n\le22\), totaling 483 complete edge columns. All assertions passed in the stated execution.

The checker does not establish the all-parameter theorem by exhaustive enumeration. The analytic monotonicity and comparison proof is in `RESULT.md`. No independent mathematical audit has been performed.
