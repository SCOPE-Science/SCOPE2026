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

# Verification

Run `python verify.py` in the same directory as `RESULT.md`, with Python 3, SymPy and NumPy installed. The script directly derives the scalar polynomial coefficients, checks all four signed squared-amplification identities symbolically with a free parameter for the number of windows, tests exact algebraic boundary points, independently executes the Parareal coarse/correction recurrence, and tests simultaneously diagonalizable three-dimensional unitary matrices. The verified execution printed `PASS: 1020 symbolic, exact-algebraic, recurrence, and matrix checks`.

These are reproducibility checks, not independent scientific audit. The analytical proof in `RESULT.md` establishes universal quantifiers and exact necessity/sufficiency; finite numerical tests alone would not. The comparisons with the original works and uncertainty about unlocated equivalent results are recorded in `REVIEW.md` and `AUDIT.json`.
