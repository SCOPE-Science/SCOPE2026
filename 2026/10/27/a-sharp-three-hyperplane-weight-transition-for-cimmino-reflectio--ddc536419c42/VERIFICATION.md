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

# Reproducibility

Run `python check.py` with Python 3, NumPy, and SymPy. The checker uses deterministic seed `230519`. It verifies the symbolic determinant, the rational branch-transition identity, the exact witness spectrum and improvement over every equal relative weighting, 4,200 arbitrary positive-weight spectral competitors (each optimally rescaled), and 350 constructed row matrices whose Gram matrices have the prescribed correlations. A successful run prints a `PASS` line.

The tests do not constitute exhaustive sampling or establish the global mathematical result by computation. The universally quantified result follows from the analytic symmetrization, three eigenvalue formulas, scalar equioscillation, and unique crossing/monotonicity proof in `RESULT.md`. This review is not independent certification.
