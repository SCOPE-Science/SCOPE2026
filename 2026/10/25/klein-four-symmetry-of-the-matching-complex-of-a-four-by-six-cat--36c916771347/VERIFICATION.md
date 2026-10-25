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

# Finite reproducibility and boundaries

Run `python3 verify_path_product.py` with Python 3 and SymPy. The script regenerates the 24 graph vertices and 30 edges, the two 15-edge components, the 383 augmented matchings per component, and 146689 augmented matchings of the full product. It exhaustively checks the directed gradient matching (190 pairs, three critical cells), calculates the oriented Morse matrix as zero, computes all rational eigenspace boundary ranks for the component-preserving half-turn, and independently checks all four signed reduced cellular Lefschetz totals. The final marker is `CATEGORICAL_PATH_PRODUCT_CHARACTER_VERIFIED`.

A finite chain enumeration by itself establishes the component rational eigenranks; the proof of the full group character additionally uses the algebraic topology of simplicial joins and the signed interchange formula. The exact Morse matching plus vanishing attaching degrees establishes the claimed integral nonequivariant wedge. No infinite-family statement, integral group lattice decomposition, or independent audit is implied.
