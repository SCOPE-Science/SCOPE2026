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

# Verification

The reproducible script `check.py` was executed against this exact package. It recomputes the rational population flux and chemical residuals; the symbolic cubic characteristic polynomial and its coefficients; all strict Routh–Hurwitz margins; the leaf-antisymmetric determinant; and a rational majorant for the logarithmic chemotactic sensitivity. It independently differentiates the original six-dimensional equations and checks the real parts of all six numerical Jacobian eigenvalues.

The infinite analytical claim rests on the explicit equations, exact rational signs, elementary two-dimensional Hurwitz criteria, cubic Routh–Hurwitz, and hyperbolic equilibrium persistence. Numerical spectrum tests alone would not establish the claim. The calculation does not certify exhaustive equilibrium enumeration, historical novelty, or independent validation.
