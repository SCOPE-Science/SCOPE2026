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

Run `python check.py` with Python 3 and SciPy. The checker evaluates the Weber-differentiated eigenvalue formula against independent quadrature, checks the trace after truncation with a quantitatively negligible numerical tail, compares small- and moderate-scale modes, and tests the Gaussian asymptotic profile on finite grids. The 71 finite assertions passed in the current package workspace. The analytical proof in `RESULT.md`, not these finite tests, establishes the infinitely many-mode and unbounded-parameter results. This file contains no independent audit or validation result.
