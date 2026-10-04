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
The proof reconstructs scalar MARINA directly from the defining update with density-matched refresh probability and independent half-dropout compression.

`verify.py` checks the scalar compressor moments, the regenerative first- and second-moment identities, the closed frontier, its client-count monotonicity, and finite-state second-moment behavior on both sides of the boundary.

Finite checks are transcription guards. The necessary-and-sufficient infinite-time result follows from the regenerative calculation in `RESULT.md`.
