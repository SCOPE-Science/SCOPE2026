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
# Reproduction and verification

The mathematical proof is the Fourier-block diagonalization, nonvanishing determinants, small-separation determinant expansion, strict modal log-concavity and monotonic endpoint comparison in `RESULT.md`. These steps establish the claim for every indicated integer degree, rather than extrapolating a finite computation.

`verify_spectrum.py` checks the exact real-matrix normalization via discrete Fourier orthogonality, with 12 SVD cases, 12 small-separation asymptotic checks and eight transition-root checks: 32 cases passed. Run `python verify_spectrum.py` with installed NumPy and SciPy. Floating-point tolerance and finite degree/radius sampling mean the script cannot certify all possible inputs or historical originality. No independent audit was performed.
