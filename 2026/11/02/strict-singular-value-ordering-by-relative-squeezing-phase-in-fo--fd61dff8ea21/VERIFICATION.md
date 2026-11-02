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

The analytic proof in `RESULT.md` evaluates two complex Gaussian integrals, establishes the exact positive Gram kernel, diagonalizes it with an entire generating family of Fock eigenvectors, and checks completeness by equality of two independently computed positive traces. Strict phase comparison follows by elementary differentiation of the larger quadratic root.

## Reproducibility

Install `requirements.txt` and run `python check_spectrum.py`. In the completed preparation the checker passed 696 deterministic assertions: matrix truncations compared the initial analytic singular values, parameterized Gram traces, and phase-ordering comparisons. The checker is supplementary finite evidence; it cannot prove claims for all nonnegative integer indices or all admissible complex parameters.

## Boundaries

The domain is the normalized one-complex-dimensional Bargmann–Fock Hilbert space, with real common scalar contraction and strict subcritical quadratic weights. The theorem concerns singular values, not eigenvalues of the nonnormal cross product. No independent mathematical audit or external certification has been performed.
