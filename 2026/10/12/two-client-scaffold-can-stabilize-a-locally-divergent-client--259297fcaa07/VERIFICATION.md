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
The package verifies the exact two-client Option-II SCAFFOLD round map.

`verify.py` compares direct client-level execution against the closed \(2\times2\) matrix, checks all three Jury inequalities over many locally contractive instances and local-step counts, and verifies the exact rational unstable-client witness.

Finite checks are transcription guards only. The all-\(K\) stability implication and the explicit supercritical witness are proved analytically in `RESULT.md`.
