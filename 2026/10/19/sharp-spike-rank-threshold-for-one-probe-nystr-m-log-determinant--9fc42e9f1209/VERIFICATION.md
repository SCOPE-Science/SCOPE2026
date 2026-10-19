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
# Reproduction checks and limits

Run `python verify.py` with NumPy installed. This standalone script constructs \(A_t\), the Gaussian Nyström matrix, its positive-definite preconditioner, and the symmetric matrix-logarithm spectrum from real eigenvalue decomposition for \(1\leq r\leq4\), \(1\leq s\leq3\), \(1\leq\ell<r+s\), and \(t\in\{1,10,1000\}\). It checks the determinant identity, the missed-spike eigenspace identity, nonnegative residual eigenvalues, the contrast-independent retained-space eigenvalue bound, and the lower/upper second-moment inequalities across 1,008 seeded finite cases.

Observed exact execution message:
`VERIFY_OK numerical_matrix_cases=1008 max_checked_bounded_remainder=17.875675 analytic_integrability_requires_proof=true`

The script uses floating-point tolerances and does not prove the universal claim. The infinite-dimensional-parameter (finite size, unbounded contrast) assertion follows from the analytic variational characterization, Gaussian covariance identity, and QR negative chi moments in `RESULT.md`. It does not verify actual stochastic Lanczos quadrature or floating-point robustness. This manuscript has not received independent audit or external validation.
