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

# Reproducibility and limits

The analytically proved theorem is in RESULT.md. `checker.py` is standalone standard-library Python and reproduces a polynomial identity after eliminating the Lagrange multiplier, checks exact rational endpoint signs and a rational bracket for the distinguished positive root, verifies the normalized coefficient vector and both equivalent formulas for the sharp constant, and prints the resulting decimal approximation.

Command: `python3 checker.py` (Python 3.9+; no external dependencies). The checker does not prove the global uniqueness of the critical point, the Hardy outer-polynomial reduction, or the infinite-dimensional extremal theorem. Those are justified by the written analytic argument and the cited full-text primary theorem. The older Suffridge chapter was unavailable for direct inspection. Independent external validation has not been performed.
