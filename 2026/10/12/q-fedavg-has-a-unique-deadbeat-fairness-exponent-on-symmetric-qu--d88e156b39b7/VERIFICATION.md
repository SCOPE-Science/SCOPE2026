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
The package reconstructs source-form q-FedAvg on two equal-curvature scalar quadratic clients with one exact local gradient step.

`verify.py` checks the scaled local-model differences and source server formula directly, compares that update with the closed Newton map for multiple positive fairness exponents, verifies one-round annihilation at \(q=1/2\) on the open interval between client minimizers, numerically checks the exact cubic coefficient away from \(q=1/2\), and verifies the global \(q=1\) map and contraction.

The finite computations are transcription guards only. Exact Newton equivalence, uniqueness of the deadbeat exponent, and the local convergence order are proved algebraically in `RESULT.md`.
