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

# Reproducible mathematical verification

The complete analytic proof is in `RESULT.md`. The standalone finite checker is `verify.py`, run with Python 3 and NumPy by `python3 verify.py` in the same directory. No input files or network services are needed.

It independently enumerates every proper labelled colouring of \(K_{r,s}\) for each \(q\in\{3,4,5\}\) and \(1\le r,s\le3\), computes two-site equality frequencies as exact rationals and directly forms the complex Fourier evaluation matrix to compare the entire probability-normalized Gram eigenvalue multiset. It further checks exact Stirling-count ratios and their asymptotic leading coefficients for ninety parameter combinations. On the packaged code, the observed output was:

`VERIFY_OK cases=27 colour_pairs=180 eigenvalues=324 words=6630 asymptotic_cases=90`

Numerical eigenvalue comparisons use an absolute tolerance of \(2\times10^{-10}\). Rational moment and count comparisons are exact. Finite tests are corroborative only and cannot establish the all-parameter theorem, whose proof rests on symmetry and exact counting. No independent mathematical validation has occurred.
