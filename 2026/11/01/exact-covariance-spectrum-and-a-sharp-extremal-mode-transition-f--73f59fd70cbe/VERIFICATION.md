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

The standalone `verify_wheel.py` was executed from the package containing the finished proof and checker. It printed `RATIONAL_INTERVAL_CERTIFICATES_OK` and `CHECK_OK`.

Checks: full exact rational covariance of uniform wheel spanning trees enumerated independently for rim sizes \(3\) through \(8\); exact rational grounded-Laplacian inversions and transfer-current covariances; Fourier eigenvalue comparisons through rim size \(14\); positivity and predicted spectral ranks through rim size \(60\); rational enclosures of \(\sqrt5\), \(\pi\) (Machin's formula), and cosine for finite crossover cases; a strict rational base inequality at \(n=11\) supporting the all-larger-size proof.

Limitations: numerical finite-frequency checks cannot certify infinite all-size statements. The infinite result additionally uses the explicit geometric-sum transforms and analytic monotonicity and asymptotic estimates in `RESULT.md`. Independent review, external certification and validation have not been performed.
