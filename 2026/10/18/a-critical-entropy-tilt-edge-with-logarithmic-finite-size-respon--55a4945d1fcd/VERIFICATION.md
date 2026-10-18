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

`verify.py` is a self-contained scientific checker requiring Python 3.10 or newer, NumPy and SciPy. Execute `python verify.py` in the directory containing the code. The completed run passed 366 assertions without reliance on external datasets: spectral eigenvalues for open skew-tridiagonal matrices; exact critical free-energy cotangent formulas; fluctuation symmetry and mean entropy production; explicit tilted-Gaussian finite-time Riccati comparisons; and large-size critical derivative formulas for three parameter choices and sizes as large as 4000.

The mathematical proof of the limit and its \(O(1)\) error is in `RESULT.md`. No finite checker tests infinitely many chain sizes or certifies originality. The entropy convention and limit order matter; neither nonlinear/disordered dynamics nor uniform-in-\(N\) finite-time deviations were verified. Independent scientific audit has not been performed.
