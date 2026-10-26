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

# Reproduction and limits

Run `python verify.py` with Python 3, NumPy and SciPy. The checker computes path graph Laplacians, validates analytic extreme eigenvectors and parity multiset identities, exhaustively enumerates all permutations for dimensions 2 through 7 using generalized symmetric eigenvalues on the mean-zero quotient, tests both odd inequalities, and samples one-point energy contraction through dimension 27. The recorded run completed 6,344 checks with no exceptions.

This finite computation does not prove the result for arbitrary length. The all-length proof uses spectral formulas, equality geometry, sorted-coordinate angular matching, and a path-crossing inequality; see `RESULT.md`. The exact odd-length constant is not proved. No independent external audit is asserted.
