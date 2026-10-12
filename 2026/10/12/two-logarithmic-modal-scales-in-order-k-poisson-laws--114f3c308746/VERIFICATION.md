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
# Verification of the two modal-scale asymptotics

Execute `python3 verify.py` using an ordinary Python 3 interpreter with the supplied `verify.py` in the same directory.

The checker uses exact `Fraction` arithmetic and two algebraically distinct coefficient constructions. It compares all coefficients through degree \(3k+2\) for 32 choices of order and rational intensity, and checks the closed polynomial for the coefficient at degree \(k\). At \(k=15\), \(\lambda=501/2000\), it confirms exactly that \(h_k(15;\lambda)<1<h_k(25;\lambda)\). Floating-point bisection tests positive crossover roots for orders 2, 3, 4, 10, 15, 50, 100, 1000, and 10000; the same root list decreases strictly. Finite evaluations of \(F(u)\) and \(Q_k(u/k)\) satisfy the upper and lower inequalities established in the proof. The low-order root at \(k=2\) agrees numerically with \(\sqrt3-1\).

Successful execution ends with `VERIFY_OK rational_coefficient_comparisons= 32 exact_k15_obstruction=True root_monotonicity_finite=True Bessel_series_bounds_finite=True`.

**Analytic limits.** No finite computation certifies the infinite asymptotics, the quantification over every positive atom, eventual modal behavior, or global root monotonicity. These are derived in RESULT.md by compound-Poisson convolution bounds, Chebyshev's inequality, exact coefficient identities, a termwise product inequality, and a standard large-argument Bessel formula. The verifier uses floating point for some finite root diagnostics; the critical order-15 inequalities are exact rational statements. No external independent validation has been performed.
