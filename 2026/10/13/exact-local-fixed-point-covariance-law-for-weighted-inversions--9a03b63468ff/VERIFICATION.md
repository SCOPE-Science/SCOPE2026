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
# Verification

The all-\(n\) theorem is proved by conditional exchangeability in `RESULT.md`.

`checker.py` exhaustively enumerates every permutation through \(n=9\). It checks each local ordinary-inversion covariance and conditional mean, the aggregate fixed-point/inversion covariance, and the weighted theorem for three deterministic weight systems.

The finite enumeration is supplementary and is not used to infer the universal theorem.
