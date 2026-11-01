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

# Reproducible checks and limits

Run `python verify.py` with Python 3 and no external dependencies. The checker enumerates all twelve cube edges and samples exact rational interior points of all maximal offset intervals determined by projected vertex levels, independent of the symbolic formula implementation. It tests positive, tied, triangle-dominant and zero projection cases, the full mean-four feasible triangle on a rational grid, the explicit inverse map, boundary nonuniqueness and the sharp variance endpoints. A successful execution prints `EDGE_CROSSINGS_AND_ALL_LAW_REGIMES_PASSED`, `EXACT_MEAN_AND_VARIANCE_BOUNDS_PASSED`, `SIMPLEX_REALIZATION_AND_INVERSE_TESTS_PASSED`, then `ALL_CHECKS_PASSED`.

Only the analytic twelve-edge crossing argument in `RESULT.md` establishes the theorem for every nonzero direction and every possible real projection ratio. Finite tests do not establish that universal claim, and no external or independent verification has been performed. The inaccessible 1991 cube-slicing antecedent remains a historical-priority risk.
