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

The standalone `verify_johnson_tail.py` rederives all four endpoint distance values from set intersections, intersects four half-planes over a unit square using rational arithmetic, and compares the resulting exact areas with both theorem formulas for several graph sizes and radii. This is distinct from counting the geometric classes by hand, but is finite reproducibility evidence rather than a proof for all parameters. The complete quantified analytic proof is in RESULT.md. The source literature provides continuous diameters but not the new near-diameter probabilities. No independent audit has been performed.
