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
The arbitrary-field proof is symbolic.

The packaged checker `artifacts/verify.py` exhaustively tests
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]

For each field it enumerates all \(2\times2\) linear maps, checks the weight-zero Rota–Baxter identity on all ordered basis pairs, enumerates all algebra automorphisms, and constructs every automorphism-conjugacy orbit.

It verifies the normal-form representatives and the exact operator and orbit counts.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem. Prime-power fields beyond the tested prime fields are covered by the symbolic proof.
