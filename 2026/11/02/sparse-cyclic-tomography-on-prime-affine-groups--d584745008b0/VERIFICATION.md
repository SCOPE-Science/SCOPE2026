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

# Verification performed

`CHECKER.py` constructs the exact \(0/1\) left-coset incidence matrix for every tested affine group and performs finite-field Gaussian elimination. Its 610 exact modular rank computations matched the theorem, with 168 exhaustive direction-subset choices on the small primes \(3,5,7\). Its 22 complex floating-point Fourier-block comparisons matched all directly constructed normal spectra, including the full-affine three-level laws at primes \(5,7,11,13\).

The proof is exact for all primes and eligible complement orders: it derives the Fourier-slice operator, treats the frequency-zero block separately, proves the required nonvanishing of every prime Fourier minor, and derives the determinant and spectral corollary. Modular rank checks can prove lower bounds for integer-matrix rational rank but are not used as universal verification. The spectral comparisons use tolerance \(2\cdot10^{-8}\) or tighter on enumerated finite instances; they do not constitute symbolic proofs.

To reproduce: `python CHECKER.py` with Python 3 and NumPy installed. This is a self-review only, not an independent audit.
