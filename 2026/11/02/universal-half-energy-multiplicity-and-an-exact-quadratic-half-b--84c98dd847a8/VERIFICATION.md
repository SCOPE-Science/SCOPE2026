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

The included `halfball_slepian_checker.py` uses the Python standard library and NumPy (`requirements.txt`). After installing the stated dependency, run `python halfball_slepian_checker.py` from the directory containing the file. Its monomial Gram matrix is calculated from explicit ball moments; the gamma-function eigenvalue and maximizing-polynomial predictions are supplied independently, rather than building the calculated operator from the claimed spectral decomposition.

The execution returned `PASS: independent monomial Gram assembly, exact half-energy counts and symmetry; 24 dimension-band tests`. It additionally checks the explicit top and bottom quadratic polynomials as generalized eigenvectors. It tested all total-degree-two monomial spaces for dimensions \(2\le d\le9\), and the paired spectral symmetry and central multiplicity for \(2\le d\le5\), \(0\le L\le3\). Numerical comparisons use absolute tolerance \(2\cdot10^{-8}\) in well-conditioned cases. Finite numerical checks cannot prove the arbitrary-degree or arbitrary-dimension statements: those follow from the algebraic parity and beta-moment argument in `RESULT.md`.

The strongest science limit is that no external independent audit or experimental validation has been completed. The historical priority search did not establish universal absence of stronger results.
