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

# Verification record

Run `python check.py` using Python 3 and NumPy, SciPy, and mpmath. The program performs fresh computations from the stated formulas: direct cotangent and Jacobian residuals; numerical quadrature of one- and two-coordinate failure probabilities; verification of the independent dilogarithm antiderivative; seeded Monte Carlo using the original three uniform longitudes and tangent-vector dot products; and numerical probes of all three asymptotic expansions. Its intended terminal output ends with `ALL_CHECKS_PASSED`.

The critical proof is analytic: the half-gap density and exact tangent criterion; the positive-simplex change of variables and nontrivial Jacobian; inclusion-exclusion of one/two failed angle inequalities; the no-solution threshold from the simplex sum; and local integration near each critical parameter. Finite numerical checks do not establish an identity on an interval. The source comparison leaves historical priority provisional; a complete inspection of several older/broader works remains unavailable. No independent mathematical audit has been performed.
