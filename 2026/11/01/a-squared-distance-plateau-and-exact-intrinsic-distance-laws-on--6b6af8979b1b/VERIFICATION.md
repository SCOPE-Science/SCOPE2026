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
# Reproducible scientific verification

Execute `python3 CHECK.py` with Python 3, NumPy and SymPy. Exact symbolic integration checks mass normalization and the quadratic and quartic expressions as polynomial identities for arbitrary formal \(s\). A direct numerical periodic-image construction checks each of 61 equally spaced source parameters, including the limiting rectangle and triangle, against the proposed four-vertex Voronoi geometry. Numerical CDF checks cover 53 parameters and 241 radius values per parameter. Five independent source-position tests use a common sample of 110,000 Haar-uniform torus targets, 550,000 source-target distances overall, and compare the exact CDF at 55 thresholds.

Successful execution recorded: all symbolic identities pass; all 61 polygon comparisons pass; all 53 CDF grids pass; all 55 target-distance CDF checks pass. Maximum observed absolute sampled CDF discrepancy: 0.003290. The sampled data do not establish all-parameter properties; exact all-parameter proof is in `RESULT.md`. No independent external audit, formal proof-assistant certification, or examination of every historical mathematical publication has been performed.
