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

# Reproducibility and scientific limits

The exact proof is in `RESULT.md`. Run `python check.py` with Python 3, SymPy, NumPy, and SciPy. Its recorded standard output is in `check_output.txt`. The script computes full-versus-cutoff radial moment matrices, exact traces and determinants, characteristic-polynomial separation, and generalized eigenvectors. It also directly diagonalizes matrices for several polyanalytic orders and nonconstant Jacobi weights, and tests deterministic complex Fourier packets against the sharp inequality. Its symbolic edge checks test the cubic asymptotics.

At completion the program printed `PASS 1812 checks; complete bianalytic spectrum, angular ordering, extremizers, sharp top gap, and all-order weighted diagnostics`. The printed count measures finite tests only. The all-order and all-weight claims follow from strict size bias, compact finite-dimensional minimax, and sector inclusion; those mathematical arguments must be checked independently of the script. Scientific originality was assessed against the relevant sources and remains best knowledge, not a claim of independent priority confirmation.
