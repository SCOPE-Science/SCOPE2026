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

# Verification of the analytic two-cycle absorption formulas

Execute `python verify.py` with Python 3 and NumPy available. The script constructs the full Hermitian graph matrix, derives normalized hub-dark modes independently from each path, checks the mode equations and orthonormality, and compares their projector diagonals with the stated general two-flux formula. It additionally tests the quarter-turn plateau and the eigenvalue count of the non-Hermitian loss generator.

The executed checks covered 169 pairs of cycle lengths between three and fifteen, four independent flux-pair choices and 10,816 sitewise probability comparisons; worst absolute discrepancy was below 5e-15. Six additional lossy-spectrum configurations satisfied the predicted dark count. These checks establish numerical consistency only, not completeness for untested graph sizes; the all-length result follows from the proof in RESULT.md. No independent audit or external validation has been performed.
