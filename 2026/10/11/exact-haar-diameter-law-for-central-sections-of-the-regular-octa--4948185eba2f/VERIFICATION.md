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

# Verification and reproducibility

The exact proof appears in `RESULT.md`. The accompanying `verify.py` runs with Python 3 and the standard library; no external data or online access is necessary.

The program verifies 215 nonzero integer-coordinate normals with exact rational squared radii; 22,000 Gaussian normals against an independent enumeration of pairwise section-vertex radii; 7 threshold comparisons against half-normal order-statistic integration; 4 independent spherical-excess calculations; 180,000 simulated normals at 3 thresholds; and 6 diameter-parameter inversions. It also checks endpoints and monotonicity numerically. The observed outcome is `VERIFY_OK`.

The angular computation uses a classical solid-angle formula; independent spherical excess and a Gaussian order-statistics integral are checks of its normalization and algebra. The proofs of extremality on orthant arcs, selection of the most imbalanced coordinate pair, six-sector reduction, and no atoms hold for all allowed normals by analytic reasoning in `RESULT.md`. Finite testing or numerical quadrature cannot by itself prove those universal statements. No independent audit has been performed.
