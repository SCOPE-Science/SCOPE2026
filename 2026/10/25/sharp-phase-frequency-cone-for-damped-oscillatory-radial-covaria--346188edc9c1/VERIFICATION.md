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

# Verification summary

The analytical argument checks all integer dimensions and all real \(\beta\) for \(\alpha,\omega>0\) via an explicit Fourier density and an exact endpoint phase criterion. In the limiting case \(\omega=0\), the radial exponential is known positive definite in all dimensions.

The independent numerical Fourier–Bessel integration in `CHECKER.py` was run for dimensions \(1,2,3,5\), with frequencies \(0.1,1,3\) and parameters \(\alpha=1.3\), \(\omega=0.51\). The exact analytic spectrum and radial quadrature agreed to typical absolute errors below \(10^{-10}\). For dimensions where the admissible interval exists, the endpoint coefficients and slight violations were sampled, confirming the predicted negative spectral sign outside. The \(d=3\) special-case algebra gives exactly \(64\pi\rho^2/(\rho^4+4)^2\).

These computations are reproducibility checks, not replacements for Bochner's theorem, the analytic half-plane continuation, or the rigorous phase sweep. The complete parameter claim is proved analytically; no finite computation establishes the strict positivity for all frequencies. Self-review is recorded separately; no independent audit has been performed.
