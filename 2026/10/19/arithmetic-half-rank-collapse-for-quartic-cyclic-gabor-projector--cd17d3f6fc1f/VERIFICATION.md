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

# Reproducible verification

Run `python verify_quartic.py` with Python 3.10+ and the NumPy dependency in `requirements.txt`. The exact checker computes exponent histograms and tests vanishing in the cyclotomic field, with no numerical zero tolerances. For each prime \(p\in\{5,7,11,13\}\), at both orders \(p\) and \(p^2\), it tests every pair \((h,w)\). That is \(46{,}592\) exact tests. Direct Hermitian Gram eigenvalues at orders \(5\) and \(7\) and two-dimensional Fourier-Gram spectra at orders \(5,7,25,49\) are compared with the analytical eigenvalue formula. The maximum discrepancy reported is below \(1.5\times10^{-14}\).

The calculation checks only the listed finite dimensions. A proof for all primes is supplied in `RESULT.md`, based on a cubic permutation obstruction, an exact prime-square stationary-phase identity and Weyl diagonalization. No independent scientific audit or external certification has been performed.
