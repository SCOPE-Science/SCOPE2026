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

# Verification of quantitative differential Hilbert approximation

Run `python3 verify.py` using Python's standard library. The embedded program reconstructs the Gauss–Legendre nodes and weights, checks positivity and exact-polynomial moments on five dyadic intervals, compares two formulas for the Bergman monomial weights, and checks decreasing finite-matrix quadrature errors in four parameter regimes.

A successful execution prints four numerical error sequences and `CHECKS_OK: 512 exact-node/weight, moment, coefficient and finite-matrix assertions`. Numerical tolerances account for floating-point arithmetic; no external packages are required.

The theoretical claim has an independent analytic proof in `RESULT.md` using Cauchy's holomorphic coefficient estimate and Gaussian quadrature exactness. Finite matrix truncations, floating-point moment comparisons and successful program execution are not proofs of an infinite-dimensional singular-number bound. The rate is an upper bound only, with constants that depend on the weights. Independent audit has not been performed.
