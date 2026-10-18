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

# Computational verification

Run `python -S verify_nm3_petersen.py` using Python 3 without external modules. The checker reads no data files and constructs the fifteen Petersen edges as five outer-cycle edges, five spokes, and five inner-star edges. It explicitly finds all 145 three-edge matchings and all 1073 augmented faces, so the finite face enumeration is exhaustive.

The deterministic edge-toggle matching yields 530 disjoint pairs. Orient every nonempty-face Hasse cover downward except selected matched covers, which are upward; a complete topological sort visits all 1072 nonempty faces. The unmatched faces comprise one vertex, ten 3-cells, and one 4-cell. The exact integer recursive elimination of matched 3/4 pairs yields the critical attaching vector `(0,0,1,0,1,1,1,1,1,1)` in a specified ordered basis, including a unit coefficient. Since no 1- or 2-cells remain, this proves a nine-sphere wedge at the homotopy level.

For symmetry, the checker explicitly constructs a graph isomorphism to the two-subset Kneser realization, then enumerates all 120 permutations in the induced `S5` action, using the orientation signs of each fixed simplex. It verifies character equality with the ten-vertex permutation character minus the constant character on every group element. The output lists the seven conjugacy-class traces. The resulting module decomposition is over rational coefficients; the checker does not establish an integral equivariant lattice isomorphism.

All computations are exact finite enumerations. No external infinite proof obligation or extrapolation remains for the stated finite graph. The computation has not been independently audited.
