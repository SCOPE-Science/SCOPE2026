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

# Reproducibility checks
Run `python verify.py` with Python 3, NumPy and SciPy. The checked package includes that exact script, and it was executed with output `VERIFY_OK 1787 geometric, quadrature and seeded checks`.

Finite geometric tests directly calculate convex hulls of independent arclength-uniform boundary samples and compare their missing perimeter with the corner-gap formula, across triangle, rectangle, pentagon and heptagon cases. Independent deterministic quadrature and seeded simulation test the right-angle corner moments and the universal rectangle benchmark. Five distinct-angle quadratures check the critical corner-MGF exponent and its coefficient, supplemented by three prescribed angle-multiplicity examples.

The exact proof in RESULT.md establishes the infinite-sample convergence, moment bounds and injectivity for all fixed convex polygons. Finite tests, simulations, and approximate quadratures do not prove or certify the infinite theorem. No independent audit has been performed; no numerical stability result for inverse reconstruction is claimed.
