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
# Reproduction checks

Use Python 3 with SymPy: `python verify.py`. The checker rebuilds the four-dimensional differential equations for the exact witness \(a=1\), \(\alpha=1/4\), \(\beta=1/100\) and computes the Jacobian independently. It substitutes exact algebraic stationary states, verifies all equilibrium residuals vanish, and compares characteristic polynomials symbolically without approximate root signs.

The symmetric polynomial factors into two negative linear roots and a Hurwitz quadratic. Each same-sign state has the same rational quartic; its four positive coefficients and both strict Routh–Hurwitz inequalities are tested as exact rational equalities. Each remaining asymmetric polarized state has a negative constant term in its characteristic polynomial, proving a positive real eigenvalue. The checker also verifies algebraically the transverse determinant identity for arbitrary positive ratio and the stationary cubic factorization.

The parameter-uniform number of equilibria is proved in RESULT.md by exact discriminant arguments, not by computer enumeration. The checks do not establish global attraction, behavior at the nonhyperbolic threshold, or that every basin intersects the physical initial-anchor plane. No independent validation has been performed.
