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

The assertions follow from a full analytical derivation in `RESULT.md`. The standalone `check_prism.py` checker uses NumPy to compare exact one-dimensional azimuthal quadrature with independent counts of all nine prism-edge crossings, integrated over spherical directions by Gauss–Legendre quadrature. The three base triangles and four heights produce twelve direct comparisons; three thin and three tall comparisons additionally check the two-scale coefficients.

Execute `python check_prism.py` with NumPy installed; the expected success marker is `PRISM_CROFTON_CHECK_OK independent_edge_counts= 12 thin_tall_checks= 6`. These finite deterministic computations are not exhaustive and cannot establish the continuum theorem; the proof controls every nondegenerate base and all positive heights. Literature-priority assessment remains conditional on reading relevant inaccessible historical sources, and no independent audit has been performed.
