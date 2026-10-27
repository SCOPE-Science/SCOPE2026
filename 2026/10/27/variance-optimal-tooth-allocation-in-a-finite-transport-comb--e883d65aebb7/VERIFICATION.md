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

The included `verify.py` constructs the killed continuous-time generator directly for each finite comb, solves the first and second moment Poisson systems in exact rational arithmetic, and compares them with the derived closed formulas. All 169 tested geometries (backbones with 1–4 edges, tooth lengths 0–3 and total tooth budget at most 5) agree exactly.

A separate exhaustive calculation for the two-tooth comb at each budget from 0 through 40 confirms both the explicit minimizer and its uniqueness. At fixed backbone length 3, enumerating all integer allocations for budgets 40, 80 and 160 gives normalized minimizing profiles approaching the analytic inverse-square-root law; these checks are finite only.

The proof for arbitrary integer budgets and the fixed-backbone large-budget limit is analytic and appears in `RESULT.md`; numerical experiments are corroboration, not a substitute for proof. No independent audit has been performed.
