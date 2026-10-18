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

# Reproducibility and mathematical limits

Run `python verify.py` with Python 3, `mpmath` and `sympy` installed. The program computes payoff indifference at 352 parameter pairs, verifies 158 consecutive positive curvature thresholds, checks 948 sign and factorization instances at 80-digit precision, checks both exact rational expected-volunteer differences, and symbolically expands the discrete curvature through order six in reciprocal group size. The program printed `PASS` after those assertions.

The positive-root uniqueness is analytically certified by the explicit polynomial derivative in RESULT.md, not by numerical bracketing. Strictly increasing thresholds are proved by the monotone ratio of two adjacent triangular second-difference kernels, not by checking finitely many group sizes. The asymptotic calculation is supported by an explicit symbolic series identity, checked by the program, together with the bounded-coefficient root argument in the proof. The program is deterministic and uses no downloaded data. Independent external review has not been performed.
