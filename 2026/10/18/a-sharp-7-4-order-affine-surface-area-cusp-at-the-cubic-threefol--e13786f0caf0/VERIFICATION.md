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

# Reproduction of exact computations

Run `python verify_affine_cusp.py` with Python 3, SymPy and NumPy. The checker, executed directly from this package, asserts the independent tangent-matrix determinant identity at a rational unit normal, all twelve signed-permutation curvature contacts, and the exact first parameter derivative and Hessian of the determinant in an orthonormal tangent chart. It also checks the singular coefficient by two equivalent symbolic expressions and prints its numeric value.

The checker includes a seeded sample of 10,000 sphere directions as a diagnostic only. Global convexity follows from the continuous great-circle Fourier bound in `RESULT.md`; a discrete sample does not establish convexity, uniqueness of contacts, or the one-sided fractional asymptotic. The limiting calculation is proved by the rescaled integral and dominated-convergence argument in `RESULT.md`, independently of numerical experiments.

The extension value and first regular coefficient are exact convergent spherical integrals, not unevaluated computational certificates. Independent scientific audit has not been performed.
