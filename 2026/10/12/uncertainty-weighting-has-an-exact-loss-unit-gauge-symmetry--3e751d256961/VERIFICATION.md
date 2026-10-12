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
The package verifies the exact task-loss scaling symmetry of source-form homoscedastic Uncertainty Weighting.

`verify.py` checks the constant objective offset, exact analytic gradient identities under independent positive task rescaling, and a full Adam trajectory conjugacy from symmetry-related log-variance initializations. It also confirms that reusing the same numerical log-variance initialization after nontrivial rescaling is not the symmetry-related state.

The computations are transcription guards. The symmetry is proved algebraically in `RESULT.md`.
