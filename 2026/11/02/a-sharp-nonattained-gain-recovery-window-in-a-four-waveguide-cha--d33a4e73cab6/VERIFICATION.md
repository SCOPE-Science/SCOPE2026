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

# Verification of the four-mode gain-recovery bound

Run `python verify.py` from the directory containing `verify.py`. It requires Python 3 with `sympy` and `numpy`. It directly recomputes the determinant from the stated propagation matrix, rederives the discriminant, tests exact critical polynomials at algebraic coupling ratios, independently diagonalizes sample propagation matrices across all claimed spectral regimes, and tests the sharp normalized-width limiting behavior.

The executable diagnostics are finite checks of algebra and sample points. The all-parameter phase classification and strict global gain-width bound rest on the proof in `RESULT.md`, not on a grid or numerical fit. Experimental or higher-dimensional Maxwell validation is not attempted. The exact endpoint Jordan conclusions use the tridiagonal eigenvector recursion in the proof.
