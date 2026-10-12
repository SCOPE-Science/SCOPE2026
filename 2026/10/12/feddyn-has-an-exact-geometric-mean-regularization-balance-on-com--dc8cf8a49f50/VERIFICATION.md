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
The package verifies the exact full-participation FedDyn recurrence on common-Hessian quadratics.

`verify.py` reconstructs the local exact minimizations and stored-gradient updates from the defining algorithm, recomputes the server state, and compares the resulting iterates with the closed formulas for the mean-client residual, client disagreement, and server error. It also checks the endpoint spectral factors, the geometric-mean minimax parameter, and the isotropic one-round cancellation.

Finite computations are transcription guards only. The all-round identities and minimax statement are proved analytically in `RESULT.md`.
