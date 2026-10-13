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
The package verifies the exact TAdam first-momentum outlier-response law at the inlier pseudo-count fixed point.

`verify.py` checks pseudo-count convergence, exact recovery of the ordinary Adam coefficient for inliers, the closed outlier attenuation coefficient over deterministic parameter grids, the unique Mahalanobis displacement maximum, and the sparse-versus-dense half-attenuation thresholds under the source default degrees of freedom.

The computations are transcription guards. The sharp influence and block-size formulas are proved algebraically in `RESULT.md`.
