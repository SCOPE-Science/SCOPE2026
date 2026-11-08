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

The proof uses the normalized monomial diagonalization, beta integral, controlled beta-to-gamma density convergence in \(L^1\), exponentially convergent Gamma Fourier series, logarithmic sample-density arguments, and the two Bergman-weight asymptotic endpoints. The exact domain is \(\alpha>-1\), \(L>0\), and \(0<\tau<L\).

Run `python bergman_log_annulus_check.py` with NumPy and SciPy installed. It separately integrates concentric annuli via regularized incomplete-beta functions and computes the equivalent Fourier coefficient formula. It compares these with the Gamma-response high-degree limit and numerical small-weight spectral widths, with explicit conservative tolerances. Numerical quadrature truncations and finite assertions are not proofs of the infinite-dimensional conclusions. The scientific limitations are in `RESULT.md`. Independent audit has not been performed.
