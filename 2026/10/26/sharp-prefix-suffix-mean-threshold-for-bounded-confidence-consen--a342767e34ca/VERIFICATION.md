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

# Computational verification and proof boundary

Run `python verify.py` with Python 3's standard library. The script performs exact rational checks of path ordering, monotonicity of cut-centroid differences, cut-gaps bounded by their initial centroids, finite freezing words for confidence strictly below the critical separation, and critical-boundary examples for three and four vertices. Its finite-state breadth does not prove an infinite-time or all-population-size statement.

The infinite theorem uses the proved order invariance; the exact prefix/suffix mean drift under an update; permanence of any inactive edge; deterministic forcing of a gap by within-block gossip below the maximum centroid separation; impossibility of exact finite block consensus for three or more ordered nodes; and standard all-edge-active randomized gossip convergence. The code is a cross-check of these algebraic steps, not a substitute for them.

The claim assumes the strict update rule `gap < epsilon`. The inclusive rule `gap <= epsilon` has different critical-boundary behavior.
