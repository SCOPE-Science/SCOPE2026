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
The package verifies the exact singular-mode dynamics of Competitive Gradient Descent on rectangular bilinear zero-sum games.

`verify.py` constructs matrices with prescribed positive and zero singular values, reconstructs the defining CGD update, checks its modal scaled-rotation formula, verifies exact preservation of the Nash-nullspace projections, and confirms the closed distance-to-Nash-set identity across multiple iterations and step sizes.

The computations are transcription guards. The global projection-selection law and sharp rate are proved algebraically in `RESULT.md`.
