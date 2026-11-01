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

# Reproducibility and verification

The embedded `verify_quadratic_cycles.py` uses Python 3 and SymPy. Run `python verify_quadratic_cycles.py` in a local environment with SymPy available. This file was executed successfully from its actual package source path.

The script symbolically verifies (i) the two-branch conjugacy to the return polynomial, (ii) the derivative and fold-curve identities, (iii) the cusp factorization and its exact translated quartic recurrence, (iv) the exact rational bistability factorization and multipliers, and (v) a special fold-boundary identity. It then checks exact Sturm root counts for 800 rational parameter pairs and performs two 250,000-step critical relaxation diagnostics.

Observed output: `PASS: return conjugacy, fold, cusp, exact three two-cycle witness, 800 rational parameter samples, critical-rate diagnostics`.

The analytical proof in RESULT.md supplies global completeness, the complete phase classification and the infinite-time critical limit. The finite parameter samples and iterates are not an exhaustive certificate for continuum parameter values or infinite-time statements. The published-priority assessment is bounded by accessible scholarly text; a later closely related manuscript's full text was not available for inspection. Independent audit has not been performed.
