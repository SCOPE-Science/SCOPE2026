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

The arbitrary-field classification is proved symbolically in RESULT.md. The exact finite-field checker `verify_r3_idempotents.py` reconstructs the quandle multiplication from \(i*j=2j-i\), enumerates every element of the tested algebras, and compares the complete idempotent set with the theorem's formulas.

Checks replayed from the packaged script:

- \(\mathbb F_2\): exactly eight idempotents.
- \(\mathbb F_3\): exactly four idempotents.
- \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\): exactly eight idempotents each.
- \(\mathbb F_9\): exactly ten idempotents, namely the parameter line plus zero.

The recorded output terminates with `CHECK_OK`. These finite calculations are consistency tests only; the general theorem rests on the symbolic factorization of the idempotent equations.
