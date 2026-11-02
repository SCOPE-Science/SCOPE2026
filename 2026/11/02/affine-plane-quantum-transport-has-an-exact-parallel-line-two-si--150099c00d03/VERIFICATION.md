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

Run `python affine_check.py` and `python symbolic_check.py` with Python, NumPy and SymPy installed. The two corresponding `CHECK_OUTPUT.txt` and `SYMBOLIC_OUTPUT.txt` files contain recorded direct outputs. `affine_check.py` constructs incidence matrices from the finite fields of prime orders 3, 5, 7 and independently compares the theorem's five-projector formula with the eigendecomposition of each full adjacency matrix. It tests 475 distinct trap placements, exhaustively all 210 unordered pairs in the order-3 plane, and all source-vertex probabilities in every tested case; maximum absolute discrepancy is approximately 5.33e-15. It also checks 56 complete incident point–line histograms.

`symbolic_check.py` verifies, with exact algebra, the point–point and line–line Gram determinants, the incident and nonincident mixed-pair determinants, the rank distinction of the zero mode for parallel versus intersecting lines, the seven mixed-incident site substitutions, and their multiplicity and trace identities. The infinite-family proof is in `RESULT.md`; it depends only on universal affine incidence axioms and exact positivity for integer orders at least three. Floating-point calculations alone would not establish the statement for every order or non-Desarguesian affine planes.

No independent human or external scientific validation has been carried out.
