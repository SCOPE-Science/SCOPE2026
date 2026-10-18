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

# Verification record

The accompanying `verify_fgm.py` runs with Python's standard library and checks the mixed logarithmic-curvature identity in exact rational arithmetic; it also checks conditional-slice normalisation, direct integral consistency, strict CDF comparisons and the sign of the likelihood curvature on a finite parameter grid. Run it from the directory containing this file with `python verify_fgm.py`.

The closed CDF expression and its derivative numerator were separately expanded using symbolic algebra, giving exact identity with the formulas in RESULT.md. The strict positivity arguments are proved in RESULT.md by elementary inequalities and an everywhere-positive Taylor series. Those universal steps—not any finite test—establish the theorem. No external independent audit has been performed.
