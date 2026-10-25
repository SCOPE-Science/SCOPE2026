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

Run `python verify_projection.py` with Python 3, NumPy, and SciPy. The checker deterministically samples 5,000 random unit directions, projects the four tetrahedral vertices, uses an independent planar convex-hull computation for the shadow area and vertex count, then compares against the exact support-face expression. It also numerically integrates exact spherical-chart radial boundaries and tests the second- and third-order coefficients at several small thresholds. Success terminates in `ALL_TETRA_PROJECTION_CHECKS_OK`.

Analytical critical steps are in `RESULT.md`: the face-projection identity, the full list of twelve minimizers, the uniform positive angular slope, the spherical Jacobian, and exact angular sector integrals. Random simulation and finite quadrature do not prove the infinite quantifiers or historical originality. This package includes no external certification or independent audit.
