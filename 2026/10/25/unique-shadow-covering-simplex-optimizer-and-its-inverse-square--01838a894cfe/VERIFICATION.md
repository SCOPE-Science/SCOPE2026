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

# Verification

Run `python3 verify.py` in the extracted package. Python 3.10+ standard library suffices for exact rational coefficient checks, numeric root bracketing, the Legendre recurrence, and checks of the rescaled limits. Optional NumPy/SciPy (versions declared in `requirements.txt`) enable the independent geometric convex-hull reconstruction. A core check ending with `SYMBOLIC_AND_LIMIT_CHECKS_OK` does not by itself prove the all-dimensional claims: those follow from the analytic orthant, real-rootedness, and uniform asymptotic arguments in `RESULT.md`.

The checker constructs each polytope from all pairwise Minkowski sums of standard-simplex vertices and compares the ConvexHull volume with the independent binomial expression, using a fixed deterministic parameter grid. No sampled volume comparison can establish the universal quantifiers. The exact cubic and Legendre recurrence checks are independently recalculated from rational arithmetic; the underlying classical Legendre-root theorem and Minkowski asymmetry theorem are explicitly invoked in the proof. No independent human or external mathematical audit has been performed.
