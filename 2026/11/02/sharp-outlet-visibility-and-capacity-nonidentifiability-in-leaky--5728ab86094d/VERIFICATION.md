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

The equilibrium elimination and slope-jump criterion were checked by direct rational computations. Run `python ffspill_check.py` from this directory to reproduce 10,720 deterministic exact-rational comparisons covering balanced and randomly branched drainage trees, all distinct activation orders for sizes up to six, finite positive coefficients, all possible visible-breakpoint counts, and full-curve nonidentifiability examples. No floating-point approximation is used. The continuous and arbitrary-size statements depend on the analytical induction and construction in RESULT.md, not on extrapolation from these finite checks. No independent verification has been performed.
