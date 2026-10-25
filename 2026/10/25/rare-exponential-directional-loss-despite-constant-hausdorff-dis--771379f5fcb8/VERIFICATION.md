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

Use `python checks/check_crown.py` with NumPy and SciPy. The checker independently reconstructs both polytopes in intrinsic coordinates for \(n=3,4,5\), validates relative volume and distance against convex-hull and constrained-optimization routines, and compares direct vertex support values to the analytic width-defect formula in 1,500 directions. Larger dimension Monte Carlo diagnostics check the exact event probabilities and expected rare positive scale; results have sampling uncertainty.

The all-dimensional volume, Hausdorff, exact probability, weak conditional limit and first two asymptotic moments follow from the supplied mathematical proof, not extrapolation from these finite tests. No independent audit has been performed.
