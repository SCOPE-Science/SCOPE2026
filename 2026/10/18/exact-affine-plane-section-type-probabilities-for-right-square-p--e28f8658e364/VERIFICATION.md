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

The checker `check.py` recomputes the polytope edge-angle mean width via independent three-dimensional convex-hull geometry and tests five aspect ratios. It also uses direct Gaussian-normal orientation samples and width-weighted offset crossings. These tests were executed successfully with NumPy and SciPy available. They do not numerically certify exact equalities or establish historical priority; those require the analytic derivation and cited-source comparison.
