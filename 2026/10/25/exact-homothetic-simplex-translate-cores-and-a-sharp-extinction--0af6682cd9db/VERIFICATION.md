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
# Verification notes

The result is certified mathematically by the barycentric positive-part proof in `RESULT.md`, not by enumeration. Every admissible threshold budget is attained by taking one facet threshold equal to the budget and distributing the remaining (nonpositive) sum across the other facets. The depth of the scaling transition follows by comparing the universal feasible barycentric requirement with the maximum attainable overlap.

Reproduce the numerical cross-check by running `python verify_simplex_floating.py` with SciPy installed. It verifies the maximum individual facet threshold against separate linear programming for all 700 listed cases. The script does not establish the theorem outside its test grid.

No independent audit or external certification has been performed.
