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
The proof is symbolic.

The packaged checker `artifacts/verify.py` verifies the parameter group over
\[
\mathbf F_q,
\qquad
q\in\{2,3,5\},
\]
including closure, associativity, inverses, the order \(q^n(q-1)\), and the stated center and derived-subgroup sizes for representative dimensions.

It independently realizes every parameter choice on \(T_3(\mathbf F_2)\) and \(T_3(\mathbf F_3)\), checks invertibility, and verifies the Hom-Jacobi identity on all ordered triples of matrix-unit basis elements.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the arbitrary-field theorem.
