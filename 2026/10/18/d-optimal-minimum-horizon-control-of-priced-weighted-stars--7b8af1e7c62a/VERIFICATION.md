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

# Reproducibility and verification boundaries

Execute `python3 verify.py` with the Python standard library. The checker constructs exact-rational star Laplacians and nonnegative stochastic transition matrices, computes their reachability matrices and finite-horizon Gramians, and compares all determinants exactly against the Vandermonde product for six different star sizes. It independently reconstructs Laguerre polynomials via their monic three-term recurrence and evaluates six discriminants using exact Sylvester resultants. Four priced two-leaf cases check the analytic Lagrange equations numerically; their universal validity follows from differentiation of the displayed closed form, not floating-point tests.

Expected successful line: `VERIFY_OK exact_star_Gramian_determinants=6 Laguerre_discriminants=6 price_KKT_cases=4`.

The finite computations do not certify infinitely many star sizes or all price vectors. These statements rely on the algebraic determinant proof, strict-concavity argument, exact Laguerre identities and standard polynomial recurrence/discriminant computation presented in RESULT.md. No independent mathematical audit or historic novelty certification has been performed.
