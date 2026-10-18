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

The analytic argument has three exhaustive cases based on the number of extreme vertices. It independently uses classical Brunn–Minkowski and Blaschke–Santaló for five or more vertices, an exact dual-hexagon shoelace computation for three vertices, and an exact four-strip square-containment equivalence for four vertices. The decisive quadrilateral equality system forces both diagonal ratios to equal \(1\); any violated constraint removes positive area from the containing square.

The standalone `check_polygon.py` executes exact-rational regression examples and verifies the four quadrilateral corner inequalities under several rational diagonal ratios. Invocation: `python check_polygon.py`. Expected success marker: `PLANAR_MAKAI_FLAG_RATIONAL_REGRESSIONS_OK`. The script does not substitute for the infinite-dimensional or all-polygon analytical arguments; in particular its sampled parameter pairs do not claim to exhaust all quadrilaterals.

External independent audit has not been performed. No assertion about higher-dimensional equality or sharpness of the many-vertex auxiliary constant is made.
