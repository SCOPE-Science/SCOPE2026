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

Run `python verify.py` in a directory containing the accompanying `RESULT.md`. Python 3 and SymPy are required. The checker asserts exact symbolic formulas for the mean, variance and sampling derivative; verifies the sharp-endpoint simplification and exact \((2,1,1/5)\) example; enumerates all binary digit strings up to length ten to verify finite-prefix expected squared errors; and compares 4,800 deterministic-seeded coordinate updates with independent residual-product and nullspace-series reconstructions.

This computation provides checks of the nonstandard algebra and finite-step implementation. It is not a proof of uniqueness of the minimizer over a continuum, the infinite-sequence uniform-digit distribution or any all-path convergence assertion; those follow from the analytic arguments in `RESULT.md`. No external scientific audit has been performed, and older potentially equivalent mathematical literature may exist.
