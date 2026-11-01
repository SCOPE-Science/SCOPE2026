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

# Verification of the two-cycle exponent spectrum

Running `python verify.py` uses SymPy and mpmath. It checks the reciprocal-quartic factorization, the reduced quadratic roots, the Jacobian trace and determinant, both exact exponent formulas, and direct two-step return for the two orbits at five representative parameters. It also numerically tests the small-deformation gap and the edge exponents as diagnostics of the proven asymptotics.

**Logical limits.** Finite parameter sampling cannot certify all parameter values, and numerical proximity cannot establish the sharp endpoint coefficients. Exhaustiveness and uniform validity instead follow from the analytic argument in RESULT.md: positivity of each derivative, nondegeneracy of every two-step fixed point, and constancy of the count along the connected deformation. The two endpoint constants follow from exact algebra and Taylor estimates. No independent review has been carried out.
