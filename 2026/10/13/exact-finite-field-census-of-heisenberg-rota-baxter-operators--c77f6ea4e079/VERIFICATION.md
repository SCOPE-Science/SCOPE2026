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
The proof is symbolic and valid over every finite field.

The packaged checker `artifacts/verify.py` exhaustively tests all linear maps for \(q=2,3\) directly against the Rota–Baxter identity at weights zero and one.

It also enumerates the reduced hypersurface for \(q=2,3,5,7\), directly rechecks every generated operator, and verifies the total and invertible formulas.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the arbitrary-prime-power formulas.
