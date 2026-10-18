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

The standalone checker `check_pentagonal_bipyramid.py` uses only the Python 3 standard library. To rerun, execute `python3 check_pentagonal_bipyramid.py` from the directory containing the proof and checker.

It computes the exact arcsine formulas numerically at six distinct heights, including the equal-edge Johnson solid and the optimizing height. For each height it samples 40000 uniformly oriented upper-hemisphere directions, calculates both the planar visible-edge count and the convex hull of the **actual orthogonal two-dimensional projections** of all seven vertices, and verifies equality. It also compares the empirical frequencies of four-, five-, six-, and seven-vertex shadows with the exact law (tolerance \(0.015\)), and isolates the stationary point by bisection.

The checker returned `PENTAGONAL_BIPYRAMID_SILHOUETTE_OK` and `UNIQUE_HEIGHT_NUMERIC_CHECK_OK` when run before packaging. The all-parameter formula, interval-ordering argument, and uniqueness theorem are proved analytically in `RESULT.md`; finite tests cannot establish mathematical exhaustiveness or historical priority. No independent external audit has been conducted.
