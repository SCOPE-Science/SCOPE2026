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
The package verifies the two-client FedExP map directly from the published server update.

`verify.py` checks the client differences, the branch condition, the fixed-point stability threshold, the exact symmetric two-cycle, and the cycle-attraction interval across many parameter values. It separately checks the exact-local-solve witness, including the FedAvg one-round solve, the FedExP derivative \(-3\), the cycle square \(1/6\), the one-step cycle derivative \(5/7\), and the two-step multiplier \(25/49\).

Finite parameter checks are transcription guards only. The threshold and cycle formulas are proved algebraically in `RESULT.md`.
