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

Run `python verify.py` in a Python environment with SciPy installed; no compiled geometric packages are needed. The script tests exact rational reflections of all generating vertices against the defining facets on an asymmetric triangular base, a square base, and a triangular-prism base whose Minkowski-center set is not a singleton. Fifteen independent linear programs minimize the dilation with unrestricted horizontal and vertical center variables, and agree with the exact formula. Both endpoint tapers are included.

The checks are finite and do not prove an all-base or all-dimensional theorem. The analytic proof in `RESULT.md` establishes the universal claim by bounding every feasible reflection from two extreme sections and constructing exact matching containment. The base equality classifications use the classical Minkowski-asymmetry bounds. Historical priority is not independently certified; specialized earlier cone/frustum literature is a residual comparison risk.
