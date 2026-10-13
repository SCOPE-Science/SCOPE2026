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
The package verifies the exact two-task PCGrad geometry.

`verify.py` reconstructs PCGrad from its two orthogonal projections, checks both taskwise directional-derivative identities, checks the aggregate norm, verifies the raw-sum if-and-only-if common-descent window and its boundaries, and tests the exact and near-antiparallel limits.

The numerical calculations are transcription guards. The identities and sharp window are proved algebraically in `RESULT.md`.
