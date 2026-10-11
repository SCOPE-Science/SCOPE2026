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

# Verification and reproducibility

The theorem follows analytically from a cube-hyperplane model, the exact exposedness of restricted coordinate functionals, a signed-sum lemma for arbitrary unequal weights, and McGregor's finite-dimensional criterion. The equality of the numerical indices of finite-dimensional dual pairs is obtained by transposition of all operators and their norming pairs.

With Python 3, execute `python verify.py` in the same directory as this file. The checker uses only the standard library (`fractions`, `itertools`), constructs every cube-section vertex with one unfixed coordinate, and checks the vertex-coordinate criterion for all integer weights from one to three in dimensions four through six. Expected output:

`VERIFY_OK rational_weight_vectors=1053 cube_vertices=42302 dimensions=4..6 weights=1..3`

The enumeration is exhaustive **only for those explicitly stated finite input sets**. It does not certify any conclusion for arbitrary real weights or larger dimensions. Those are covered by the proof in `RESULT.md`. The result is restricted to positive weights, real Banach spaces, and cycles with at least four vertices; no exact nonmaximal numerical index is asserted.
