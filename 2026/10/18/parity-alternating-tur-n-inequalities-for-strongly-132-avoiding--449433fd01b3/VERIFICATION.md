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

Run `python3 verify_turan.py` using only the Python 3 standard library. It constructs the published algebraic generating function by exact integer-series operations, checks its initial coefficients, independently counts permutations of orders one through eight by the defining avoidance test, and prints the result. The script checks signs of the Turán determinant for the *finite* indices 8 through 239 and approximate convergence of three normalized ratios.

The finite computation cannot prove the infinite sign theorem, nor does it prove the first eventuality index. The infinite proof uses the explicit two-point local expansions, analyticity and singularity transfer in `RESULT.md`. The exact arithmetic check verifies the algebraic input at finite orders; numerical floating-point evaluations of the asymptotic constant are supplementary.

The data are generated in the script, with no external packages, remote services, or files needed.
