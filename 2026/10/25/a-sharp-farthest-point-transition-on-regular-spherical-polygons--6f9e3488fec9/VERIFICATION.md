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

The algebraic proof in `RESULT.md` is self-contained for all integers \(n\ge3\) and radii \(0<\rho<\pi/2\). Re-check the vertex dot-product extrema \(m\), the geodesic-edge normalized chord norm interval \(c\le L\le1\), and the equality cases under \(m>0\), \(m=0\), \(m<0\). The test script `spherical_vertex_check.py` requires Python 3 and NumPy; execute `python spherical_vertex_check.py` to sample 1001 points on each boundary edge for 32 independent input pairs, and assert discrepancy below \(2\times10^{-6}\). All 32 combinations passed in this review. Sampling cannot certify universal quantifiers, prove absence of other maxima, or establish originality. The extremal shape is the continuum geodesic hull; no polyhedral-surface shortest paths are considered. Independent audit is not performed.
