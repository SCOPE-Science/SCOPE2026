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

Execute `python checker.py` with Python 3, NumPy and SymPy. The script uses exact rational/symbolic arithmetic for the orthogonally invariant identity, the axisymmetric latitude factorization, and the explicit off-axis maximizer, including its eight boundary points and sharp surface area. It also tests 300 independent generated exact-solvability configurations numerically by the explicit phase construction.

The analytic proof in `RESULT.md` establishes the theorem for **all** real positive-definite matrices in dimension three and all unit directions. The finite numerical test is only a consistency check; it cannot establish all-input claims or novelty. The checker does not invoke an external proof system. No independent validation, external certification, or higher-dimensional result is asserted.
