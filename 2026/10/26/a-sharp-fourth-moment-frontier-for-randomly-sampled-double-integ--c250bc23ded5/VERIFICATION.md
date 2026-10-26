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
# Verification of the sampling-moment frontier

`verify.py` uses exact SymPy rational arithmetic to check the five-point probability vectors, moments of orders zero through four, the covariance matrix for the stated gains and fixed lower moments, the signed determinant factor, and the positive-definite Lyapunov matrix satisfying a strict unit residual. It also symbolically derives the fourth-power coefficient for arbitrary real feedback gains and arbitrary symmetric input matrix.

Run `python verify.py` in a Python environment with SymPy installed. A successful run prints confirmation and exact threshold values. The proof of the infinite class uses positive-map spectral-radius monotonicity and a cone Perron eigenvalue crossing argument; the script verifies the computational premises, not those general theorems. No independent audit has been performed.
