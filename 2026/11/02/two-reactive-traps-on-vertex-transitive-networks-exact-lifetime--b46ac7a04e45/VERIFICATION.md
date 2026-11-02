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

## Reproducibility

Run `python verify.py` with Python 3 and NumPy. The checker independently constructs the killed Laplacian and computes the mean by a direct linear solve, comparing it to the Green pseudoinverse formula for cycles, complete graphs, hypercubes, and square tori, at unequal random reaction rates and equal-rate optima. It also checks the exact 3-by-3 torus Green diagonal and two distinct resistances.

## Proof boundary

The proof in `RESULT.md` establishes the theorem universally; the checker verifies only finite examples and does not constitute an infinite certificate. The self-review is recorded in `REVIEW.md` and `AUDIT.json`; no independent validation has been performed.
