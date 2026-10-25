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

Run `python verify.py` with NumPy and SciPy. The program checked five mathematical dependencies: (i) projection-area equality against planar convex hulls and the cone criterion for silhouette type; (ii) the spherical side-segment formula against direct spherical quadrature at six thresholds; (iii) triangular-silhouette area-tail probabilities against 1,900,000 Haar viewing directions; (iv) recovery of the known first marked area moment via tail integration; and (v) recovery of the known second marked area moment. It finished with `ALL_MARKED_TETRAHEDRAL_SHADOW_CHECKS_OK`.

These finite computations test consistency and numerical normalization; the exact all-threshold theorem is established by the deterministic spherical-cap proof in RESULT.md. The claim is not formally machine-certified, and no external independent audit has been performed.
