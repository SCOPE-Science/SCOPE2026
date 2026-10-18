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

A standalone `check.py` independently constructs the exact cube-slab polytope in dimensions 2, 3 and 4. It enumerates exact rational vertices from active hyperplanes, uses `scipy.spatial.ConvexHull` only for facet triangulation, and evaluates simplex volumes and second moments exactly via SymPy rationals. Comparisons of volume, the transformed anchored-coordinate covariance matrix, its inverse, and the strict negative increment covariance passed all 18 test combinations with \(t\in\{1/2,1,3/2,2,5/2,4\}\).

The general formula additionally has an analytic proof from the uniform-sum characteristic function, convolution identity, exchangeability, symmetry-unimodality, and matrix inversion. The functional limit uses Donsker's theorem and a positive-probability endpoint conditioning event; finite exact tests do not prove that limit. No arbitrary thin-endpoint functional bridge limit is asserted. No external or independent scientific audit has occurred.

Run from the package root: `python check.py` (requires Python, NumPy, SciPy, and SymPy).
