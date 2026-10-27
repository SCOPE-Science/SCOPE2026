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

# Verification of the quadratic-exponential ambiguity threshold

`checker.py` reconstructs the polynomial and the quartic shifted Hurwitz determinants using exact symbolic arithmetic. It checks the seven coefficient identities for the third Hurwitz determinant, each coefficient of the second determinant, the exact critical constant and both conjugate critical roots. Four independent high-precision numerical integrations are compared against the closed ambiguity formula; representative supercritical zeros at three coefficients are solved numerically, with residuals displayed in `checker_output.txt`.

Run `python checker.py` with dependencies from `requirements.txt`. The stated results are reproducible from the packaged files. The polynomial-root continuity and all-real-parameter positivity arguments are analytic deductions explained in `RESULT.md`, not numerical conclusions. The numerical integral tolerance allows error in oscillatory infinite-tail quadrature; the exact symbolic identities are asserted at algebraic equality.

Independent audit not performed. Uniqueness and counts of supercritical off-axis zeros remain unproved; publication priority has not been independently certified.
