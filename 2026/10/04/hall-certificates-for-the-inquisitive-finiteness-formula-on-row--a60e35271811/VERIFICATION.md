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
The semantic proof was reconstructed from the binary-team clauses in the primary source and the infinite Hall theorem for families of finite sets.

`verify_hall_certificates.py` uses only the Python standard library. It exhaustively verifies Hall's criterion against explicit systems of distinct representatives for all set-families in its small finite test range. It also checks finite truncations of the boundary relation: after deleting the special right value, every proper subset containing the special left vertex satisfies Hall's inequality, while the only deficiency is pushed to the whole finite truncation. Expected output: `VERIFY_OK`.

The script is finite evidence only. The arbitrary-cardinality theorem and the infinite counterexample are established by the written proof.
