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

The mathematical proof uses the standard contents of the symmetric-group transposition-class sum and the Pieri decomposition under restriction to the two vertex parts of a complete bipartite graph. For each specified Young diagram the legitimate two-box removals are fully enumerated in RESULT.md.

Execute `python verify.py` with Python 3 and NumPy installed. The checker evaluates both exact two-box Pieri eigenvalue predictions on the range 6 through 20 inclusive, then independently assembles Specht seminormal adjacent-transposition matrices and the complete crossing-edge Laplacian for each n from 6 through 10 inclusive. The eigenvalues computed directly agree to numerical tolerance with the exact formulas.

These tests are finite checks and do not certify unbounded-n statements. The proof is the classical algebraic argument in RESULT.md. Source priority and complete mathematical correctness have not been independently audited.
