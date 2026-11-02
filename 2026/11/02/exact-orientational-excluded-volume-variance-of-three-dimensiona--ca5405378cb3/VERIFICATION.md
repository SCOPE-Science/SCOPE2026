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

Install dependencies from `requirements.txt` and run `python CHECK_EXCLUSION.py`. Deterministic pseudo-random seed 901847 generates 240,000 uniform rotations using SciPy's rotation sampler. Empirical Haar absolute-entry moments are compared with the exact values \(1/3\), \(2/(3\pi)\), and \(8/(3\pi^2)\). The means and variances of the excluded-volume formula are checked for the lengths \((1,1,1)\), \((2,1,1)\), and \((2,3,4)\). A separate convex-hull calculation of all 64 sums of corner pairs tests nine rotated Minkowski sums independently of the analytical zonotope-volume computation.

The completed checker produced `ALL_EXCLUDED_VOLUME_CHECKS_PASSED`. The cube's exact normalized variance is \(-69+96/\pi+384/\pi^2\). This code is a diagnostic; the universal theorem is proved by the determinant identity, exact Haar integrations, and the nonnegative variance decomposition in `RESULT.md`. Sampling error and floating-point error cannot establish a universal inequality.

The novelty comparison reviewed open primary texts on orientationally averaged exclusion volume and checked related results. Complete historical priority and independent mathematical verification remain unestablished.
