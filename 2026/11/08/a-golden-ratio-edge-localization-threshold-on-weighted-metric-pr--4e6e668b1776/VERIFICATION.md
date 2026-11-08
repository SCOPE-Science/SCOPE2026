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

# Verification record

The analytical proof establishes the result for every integer \(n\ge3\) and every real \(h>0\). In particular, the strict crossover proof is an all-parameter derivative inequality, not a numerical sample or a graph enumeration.

The standalone `prism_poisson_checks.py` uses a refined graph and exact-rational Kirchhoff Poisson equations. It introduces each evaluation point as an extra vertex, solves the resulting zero-total-mass forcing with a fixed gauge, integrates the edgewise quadratic to restore mean zero, and compares the resulting Green diagonal with the claimed closed spectral formula. It tests four circumferences \(n=3,4,5,6\), three positive rung lengths \(h=1/3,1,5/2\), and five locations per graph (one vertex, two edge midpoints, and two other edge-interior coordinates).

Invocation: `python prism_poisson_checks.py`.

Observed output: `EXACT_REFINED_KIRCHHOFF_POISSON_CHECKS_PASSED 60`.

The finite checks corroborate normalization, the point-mass convention, edge-coordinate dependence, and the two edge-orbit formulas; they are not substitutes for the infinite proof or independent verification. Literature priority has been checked against the cited accessible primary work and targeted mathematical-record searches, but additional unindexed coverage is possible.
