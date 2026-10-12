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
The package reconstructs the original FedAvgM update on identical scalar quadratic clients.

`verify.py` checks the exact state matrix, every fixed-workload Jury inequality, the two-round monodromy trace and determinant, the necessary-and-sufficient periodic stability condition, and the exact rational witness. It also confirms that the same one-versus-two-step workload is stable for vanilla FedAvg.

Finite random checks are transcription guards only. The infinite-time stability claims follow from the analytic Jury argument in `RESULT.md`.
