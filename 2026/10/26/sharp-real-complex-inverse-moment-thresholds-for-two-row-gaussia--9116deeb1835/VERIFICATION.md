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

# Verification and reproducibility

Execute `python verify.py` from this directory using Python 3 standard library. The program evaluates 1,305 exact-rational and finite-dimensional algebraic checks: the two-row Cauchy–Binet Gram determinant identity, exact rank-one geometric-sequence degenerations and nearby residual coordinates, and rational LDL positivity of the worst-convolution tridiagonal covariance. It prints a `VERIFY_OK` message on success. This is an independently re-executable finite check, not a certificate for continuum or probability assertions.

For the infinite theorem, check these proof obligations against `RESULT.md`: (i) the tridiagonal convolution eigenvalue bound uniform over projective row directions; (ii) the Beta-projection small-ball exponent \(\beta m\) and projective covering number of order \(t^{-\beta}\); (iii) integrability of the Gaussian radius inverse power \(\beta(m-1)\); (iv) the triangular real or complex residual-coordinate Jacobian and positive density on the bounded chart; (v) the matching layer-cake moment criterion.

The code tests do not establish uniqueness of the finding, calculate an exact tail constant, or assess closed-loop data-driven control stability. Independent scientific validation has not been performed.
