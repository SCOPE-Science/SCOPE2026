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

The universal result is proved analytically in RESULT.md. The checks below provide independent computational consistency tests rather than a finite certification of the all-frequency claim.

To reproduce: run `python verify_projective_kernel.py` with Python 3 and `mpmath` installed. The checker evaluates Fourier integrals by independent quadrature and compares against the gamma-series expansion, then verifies expected signs and finite-grid negative spectral witnesses. The checker reports: `PASS: 63 Fourier comparisons, asymptotic-sign checks and finite negative witnesses`.

The explicit spectral witness is a Fourier mode on an equally spaced projective circle, where negative continuous Fourier coefficients imply negative finite circulant eigenvalues for sufficiently fine sampling; the actual checker tests selected grids only. Symbolic Fourier asymptotics and the even-power Hilbert-space Gaussian argument are given in the proof and are not delegated to the program.

Scope limitations: positive concentration, positive exponent, finite projective dimension at least two over the three named scalar fields. The numerical checks are not an infinite sign proof. Independent audit not performed.
