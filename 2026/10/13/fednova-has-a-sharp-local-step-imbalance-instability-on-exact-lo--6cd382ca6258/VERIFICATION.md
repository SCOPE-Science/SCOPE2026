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
The package verifies the exact two-client vanilla FedNova round in the locally solved quadratic regime.

`verify.py` reconstructs each client trajectory, computes the normalized local gradients and default server scaling, compares the direct update with the closed affine map, checks the exact local-step-ratio stability criterion over many integer pairs, and verifies the \(1:6\) rational divergence witness and its displaced fixed point.

Finite computation is used only as a transcription guard. The fixed point and the if-and-only-if stability frontier are proved algebraically in `RESULT.md`.
