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
# Reproduction checks and proof limits

Execute `python verify.py` in an environment with the versions specified in `requirements.txt`. The test implements the theorem's dilogarithm expression and computes the same moments by numerical integration over a uniform angular direction. It also reconstructs Gaussian Nyström preconditioners and the preconditioned matrices after independent orthogonal rotations, comparing the matrix logarithm against the exact scalar determinant formula and the two-step Lanczos expression. In the high-contrast regime it integrates the *excess* over ideal spectral preconditioning in a scaled Cauchy variable; naive fixed-angle quadrature is not accurate enough to resolve rare directions.

The expected successful result is `VERIFY_OK` with counts `100` independent angular integrals, `480` direct-matrix orientations, `480` two-step Lanczos tests, and `4` spectral-gap scales. All computations use ordinary finite-precision scientific software. A finite test is not an exhaustive proof, does not certify an infinite limit, and is not evidence of novelty. The mathematical proof in `RESULT.md` establishes the exact and asymptotic claims for every stated input. An independent audit has not been performed.
