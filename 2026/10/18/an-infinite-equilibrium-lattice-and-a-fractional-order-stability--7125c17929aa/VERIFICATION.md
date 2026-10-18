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

# Reproduction and scope

Execute `python3 CHECK.py` in the directory containing the program. It requires only the Python standard library and prints the number of passed finite numerical consistency assertions. The program tests the explicit equilibrium branch parameterization, algebraic identities for Jacobian determinants, paired determinant levels, eigenvalue stability comparisons, and exact level-count formula over parameter grids. These finite checks serve as diagnostics; they neither establish infinite enumeration nor certify asymptotic claims.

The complete infinite classification follows instead from the sine equation, exact Jacobian determinant calculation, spectral generating-function boundary, strict threshold monotonicity, and integer level counting in `RESULT.md`. The spectral stability theorem is a prior general result quoted in the primary paper; no independent external validation of the new mathematical findings has been performed.
