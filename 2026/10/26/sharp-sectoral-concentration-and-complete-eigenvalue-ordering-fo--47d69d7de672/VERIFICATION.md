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

The self-contained scientific statement and analytical proof are in `RESULT.md`. With Python 3, NumPy and SciPy installed from `requirements.txt`, run `python verify.py` in the same directory. The script independently integrates normalized associated Legendre functions by Gauss–Legendre quadrature, compares exact Wallis-product formulas, diagonalizes fixed-order hemispherical restriction matrices, checks the strict order chains and confirms the sharp expression for the maximal eigenvalue over tested degrees.

The submitted `verification_output.txt` reports 630 cross-degree overlap comparisons, 136 independently assembled two-dimensional spectral blocks, and exact formula-based monotonicity checks over 300 integer degrees. It reports largest integral discrepancy below \(2.21	imes10^{-14}\). The tests are finite; the infinite theorem is established by the analytical Sturm–Liouville, central-binomial and ratio arguments in the proof. No independent mathematical audit has been performed.
