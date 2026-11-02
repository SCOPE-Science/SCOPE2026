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

# Reproducibility and verification

Run the independent finite checker from the extracted complete package directory with `python3 verify.py` (Python standard library only). It numerically integrates the two full and inner-half Gram matrices using Simpson quadrature, solves the two-dimensional generalized eigenvalue polynomial, and compares against the closed spectral formula for five annulus moduli and nine Fourier degrees. The checked execution returned `PASS: 271 finite checks; analytic proof required for all-mode statements.` It also tests ordering and the limiting exponential profile at selected values.

The exact integral evaluations, nonzero Gram determinants, zero-mode calculation, power-series positivity of the derivative numerator, and exponential spectral-tail counting are given explicitly in RESULT.md. These are analytic arguments for all positive moduli and all Fourier modes. Finite samples neither establish those infinitely quantified statements nor independently validate originality.

The source anchor for the middle-period literature is arXiv:2303.12137v1, first publicly posted 2023-03-21. Potential historical overlap with a 1994 annular Toeplitz/Hankel paper has not been eliminated because full text was not accessible. No independent mathematical audit or validation has been performed.
