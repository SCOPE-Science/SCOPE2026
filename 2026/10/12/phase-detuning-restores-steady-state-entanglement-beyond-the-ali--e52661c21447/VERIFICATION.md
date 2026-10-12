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

# Verification details

The mathematical proof is in `RESULT.md`. The packaged `check_symbolic.py` verifies the finite algebraic identities in the covariance determinant and in the exact scalar phase optimum, using `sympy`. It executed successfully and printed `SYMBOLIC_OK`. The finite test program `verify.py` (with `numpy`, as listed in `requirements.txt`) constructs the drift matrix and bath diffusion covariance directly, solves a real \(4\times4\) steady Lyapunov equation, performs partial transposition on the second momentum quadrature, and computes the smallest eigenvalue modulus of \(i\Omega V^{\Gamma}\). The comparison formula is evaluated separately from these matrix operations.

The numerical script executed successfully from the packaged source with output beginning `VERIFY_OK`. It checks 1,500 reproducible random parameter configurations and fixed-coupling phase scans, including points beyond the phase-optimization threshold. The calculations are floating-point cross-checks, not rigorous enclosures or an exhaustive search over all continuous parameters. Exact covariance block determinants, nonnegative square-root selection, strict convexity and the quadratic entanglement inequality prove the universal statements on paper. No external independent audit or certification has been performed.
