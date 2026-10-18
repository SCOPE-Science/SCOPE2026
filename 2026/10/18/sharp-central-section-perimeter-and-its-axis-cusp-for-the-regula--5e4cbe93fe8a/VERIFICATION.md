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

# Verification

The included Python 3 program independently intersects all twenty-four exact vertex-to-axis edges with the given central plane, constructs a planar convex hull, and calculates its perimeter. It compares this with the explicit six/eight-chamber formulas at 3,200 deterministic nondegenerate orientations (1,594 six-sided; 1,606 eight-sided), with maximum absolute discrepancy 5.329070518200751e-15. It also checks the global Jensen projection bound and its angular stability lower estimate, special exact orientations and the linear cusp coefficient at three small scales. All checks passed when executed from the packaged source. Execute `python verify_rhombic_perimeter.py` to replay. These finite comparisons do not prove the all-direction assertions: the supporting mathematical proof is the exact tetrahedral-generator projection inequality and the exhaustive combinatorial edge formula. No independent external audit has been performed.
