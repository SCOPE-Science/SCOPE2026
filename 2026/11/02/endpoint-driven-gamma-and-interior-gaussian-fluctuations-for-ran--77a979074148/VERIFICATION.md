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

The proof is analytical. All identities are stated for every integer \(n\ge3\), strictly convex quadratic coefficient \(a>0\), interval length \(\ell>0\), and arbitrary affine coefficients.

`python checks/verify.py` was run from the package directory. It confirmed exact rational moment expansions for each integer \(n=3,\ldots,350\), independent monotone-chain/ shoelace area reconstruction at sample sizes 3, 4, 7, 13, and 25, seeded finite-sample moment comparisons for both endpoint designs at sample sizes 3, 5, 12, and 30, and variance-scale computations through sample size 100000. It printed `ALL_PARABOLIC_ARC_TESTS_PASSED`.

Exact rational checks test finite identities; the analytical geometric secant calculation, beta–Dirichlet factorization, extreme-order-statistic limit, and exponential delta-method calculation prove the theorem. Finite sampling does not prove the infinite limits. Priority of the exact geometric combination is provisional; no independent mathematical audit has been performed.
