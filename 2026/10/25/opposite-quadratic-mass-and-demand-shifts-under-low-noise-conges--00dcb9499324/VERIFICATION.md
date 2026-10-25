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

# Verification of the stated asymptotic

Execute `python3 verify.py` from this directory using Python 3 and the standard library only. The checker solves each scalar logit equilibrium by 56 bisection iterations, with 8192-step composite Simpson quadrature for mass and weighted demand. It reports 174 passed assertions across 27 smooth two-moment parameter triples and three explicitly checked non-potential witness noise levels. It compares differences divided by the square of the noise scale against the analytic coefficients, tests the predicted sign reversal and checks the linear assignment norm constant in the witness.

The analytical proof separately proves uniqueness, the exact logistic variance, uniform exponentially small boundary tails, the implicit fixed-point coefficient and the sharp assignment norm. No finite grid proves all possible congestion functions or every noise scale. Publication novelty has not undergone independent review.
