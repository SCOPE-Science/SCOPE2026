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

# Reproduction and limits

Run `python artifacts/verify.py` with Python, SymPy and mpmath. The checker verifies exact Gaussian Fourier-moment reconstruction of the Wigner polynomial, exact critical circle factorization, both Hessian eigenvalues at both junctions, all sampled radial-discriminant regimes, four numerical evaluations against independent direct Wigner oscillatory integrals, and the exact negative-point polynomial used in the logarithmic-volume proof. Every check passed on the supplied file.

The infinite domain-topology and asymptotic claims follow from the analytic polar-discriminant, critical-point and Gaussian upper/lower-bound proof in RESULT.md; finite numerical checks do not certify an infinite assertion. The polynomial Hessian (rather than the Hessian of the Gaussian-weighted Wigner function) is quoted for exact integers; multiplying by a positive factor does not change the saddle signature.

Independent mathematical audit has not been performed.
