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

The argument is independent of finite enumeration: determinant edge equations, nonzero-root tree induction, cycle subdivision and contraction, a forced-zero obstruction and the spanning-tree two-bracket decomposition are proved in `RESULT.md`.

Run `python verify.py` to enumerate every assignment of two vertex-coordinate vectors over small prime fields. Tests include a triangle, a triangle with a leaf, a square with one leaf, a square with opposite leaves, and a square with adjacent leaves, with cases over \(\mathbf F_2\) and \(\mathbf F_3\). The exact expected image sizes are checked, not sampled, and for width-two examples the sums of two brackets are exhaustively confirmed to reach every center vector. The successful program prints `VERIFY_OK`.

These finite computations do not establish surjectivity for infinitely many graph sizes or all fields. The all-field claim rests on the explicit constructive proof. Independent audit has not been performed.
