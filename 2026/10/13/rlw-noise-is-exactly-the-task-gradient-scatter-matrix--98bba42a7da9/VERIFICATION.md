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
The package verifies the exact second-order geometry of exchangeable Random Loss Weighting.

`verify.py` constructs finite exchangeable simplex laws, computes their exact empirical weight covariance, pushes it through fixed task-gradient matrices, and checks the centered-scatter formula, pairwise energy identity, covariance rank, two-task specialization, and the sharp one-hot upper endpoint.

The computations are transcription guards. The covariance and extremal statements are proved algebraically in `RESULT.md`.
