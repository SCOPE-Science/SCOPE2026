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

The mathematical proof is the explicit universal elementary-collapse sequence in RESULT.md. The numerical checks below corroborate selected cases rather than establishing any universal statement by extrapolation.

Execute `python verify.py` after installing the dependencies in `requirements.txt`. The script enumerates the entire dual face complex in each test graph, validates every elementary free-face removal against the current face poset, compares the final survivor with the constructed square filling plus distance-at-least-three edges, and computes exact integer Smith forms of the square-filling cellular boundary.

Expected results: the three-page square book has three squares and contractible square filling; the three-cube has six squares, second Betti number one and four long edges; the four-cube has twenty-four squares, second Betti number seven and forty long edges; two cube boundaries glued along a square face have eleven squares, second Betti number two and twenty long edges. The rectangular grid has zero second Betti number. The toroidal five-by-five grid has second Betti number one, first Betti number two and 150 long edges. The twisted five-by-five grid has first Betti number one, zero second Betti number, and one Smith factor of two, exhibiting integral two-torsion.

The executable verification marker is `SQUARE_FILLING_THREE_CUT_COLLAPSE_AND_INTEGRAL_CHECK_OK`. The program does not validate a complete literature search or prove the theorem for graphs that are not tested.
