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

The accompanying `verify.py` performs exhaustive small-case checks over actual binary-extension field algebras. It enumerates all vector subspaces, tests multiplicative closure, then counts ordered complementary pairs and compares the count against the stated degree-product formula. For total algebra dimensions at most four it checks the Rota–Baxter identity and idempotence at every pair of elements for every associated projection.

The tested degree multisets are `(1)`, `(2)`, `(3)`, `(1,1)`, `(1,2)`, `(2,2)`, `(1,1,1)`, `(1,1,2)`, `(1,3)`, `(1,1,1,1)`, `(1,1,1,2)`, `(2,3)`, `(1,4)`, `(1,2,2)`, and `(2,2,1)`. Run `python3 verify.py`; it must end in `VERIFY_OK`.

Finite checks do not establish universal validity. The arbitrary-prime-power theorem follows from the algebraic decomposition, Frobenius invariance, weighted matrix-tree theorem and block determinant evaluation in `RESULT.md`. Nothing here represents external or independent validation.
