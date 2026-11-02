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

# Reproducibility

Run `python checker.py` using Python 3, NumPy, SymPy, and SciPy. The checker tests exact symbolic first and second derivatives of the fractional-programming summands and exercises 210 random metric stars (degrees 3–8), verifying positive optimal rates and matching 2,520 alternative feasible allocations. The numerical solver is a diagnostic and not a proof of the infinite-domain theorem. Reconstruct the analytical proof by solving the one-dimensional Poisson problem on each arm, imposing the Kirchhoff condition, and applying strict convexity plus the positivity contradiction. Only self-review has been performed.
