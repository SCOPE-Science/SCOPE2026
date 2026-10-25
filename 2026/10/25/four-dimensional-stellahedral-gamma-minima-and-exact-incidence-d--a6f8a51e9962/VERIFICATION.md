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

# Reproduction

Run `python3 verify.py` using Python 3.9 or later; no third-party packages are required. The program reconstructs each face poset by intersecting defining facet-vertex sets. It derives all 16 flag \(h\)-coefficients by inclusion-exclusion, compares the full noncommutative \(ab\)-index with the proposed \(cd\)-index, and independently applies the Catalan-polynomial gamma map stated in Proposition 6.3 of the cited paper. It verifies the defect formulas and equality implications for the four-simplex, four-cube, four-cross-polytope, three simplex products, and two four-dimensional pyramids.

Successful output terminates in `EXACT_OK basis=5 convex_4_polytopes=8`. Arithmetic is integral and exhaustive within each of the eight finite face lattices; no floating-point tolerance is involved. The checker establishes neither exhaustive four-polytope coverage nor historical originality. The universal proof is in `RESULT.md`; the published universal gamma transform is a cited mathematical input.
