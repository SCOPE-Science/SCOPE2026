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
# Reproducibility and scope

`verify_rectangle.py` uses only Python's standard library. Execute it in the same directory with `python verify_rectangle.py`. It enumerates the vertices of the four-corner Lipschitz dual polytope by intersections of triples of active distance constraints, then checks all 22 unordered pairs with at least one new midpoint, at 19 positive aspect ratios. The script recomputes positive extension measures from the displayed formulas, checks coefficients and normalization, compares every computed extremal ratio with the analytic constant, and checks new-to-new ratios are at most one.

Observed execution: `VERIFIED aspect_ratios=19 target_pairs=418 analytical_formula_matches=yes`. This is numerical evidence, not interval arithmetic or an all-real proof. In particular, the analytic symmetrization, transport convexity, and strict-log-concavity arguments in RESULT.md, not this finite enumeration, supply the universal quantifiers. The root approximation is numerical; only uniqueness is mathematically asserted. No independent audit has been performed.
