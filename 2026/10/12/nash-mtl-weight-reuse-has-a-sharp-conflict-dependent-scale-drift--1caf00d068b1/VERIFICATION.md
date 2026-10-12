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
The package verifies the two-task Nash-MTL stale-weight scale-drift theorem.

`verify.py` checks the exact positive Nash weights, fresh scale invariance, stale taskwise projections, the sharp common-descent interval and its boundary cases, and randomized conflict geometries.

The computations are transcription guards. The universal result is proved algebraically in `RESULT.md`.
