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

# Reproducible verification

Run `python verify_rank_order.py` with Python 3 and NumPy, SciPy and SymPy installed. Observed output: `PASS: 11 symbolic identities; 54 numerical assertions`.

The symbolic script reconstructs the first and second Taylor coefficients of the rank-one and rank-two projected Lyapunov vector fields from the independent initial projectors, and checks the negative-direction coefficient exactly. The numerical portion integrates both fixed-rank flows independently and checks positive semidefiniteness, comparison with the full covariance and indefiniteness of their rank difference at six small positive times. It also verifies the predicted quadratic leading coefficient with a stated numerical tolerance.

The script tests only examples and algebraic identities; the theorem for all admissible positive-semidefinite noise matrices satisfying the nonzero coupling hypothesis follows from the analytic factorization and Taylor proof in RESULT.md, not from finite sample coverage. All computations use exact arithmetic symbolically and floating-point ODE integration only for supplementary tests. Independent audit has not been performed.
