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

# Exact computational verification

Run `python3 c8k3_symmetry_verify.py`. Standard-library Python only; no third-party tables or network access.

The algorithm recreates the 24-vertex adjacency relation and all 18,722 independent faces, including the empty face. It verifies the complete face vector; all 9,358 elementary matching pairs; exact acyclicity across 104,592 directed covering relations; the six remaining critical faces in degrees four and five; the exact integral rank-one primitive Morse differential; and the chain boundaries and Morse projections of integral lifted representatives.

For all 96 elements of \(D_8\times S_3\), it computes the action on homology by signed simplicial transport of genuine lifted cycles. The resulting degree-four and degree-five traces match the claimed formulas. As a cross-check, signed fixed-simplex Lefschetz traces are enumerated independently and equal the alternating sum of the two homology characters for every element.

Expected final output: `C8_K3_EQUIVARIANT_HOMOLOGY_VERIFIED 18722 9358 6 96 boundary_rank_1 H4_1 H5_3`.

These checks are **exhaustive for the defined finite complex**, not an argument for arbitrary cycle length or color count. They do not establish an integral equivariant group-lattice classification. The homotopy argument uses elementary cancellation of a primitive 4/5 cellular attaching map after the integral Morse reduction.
