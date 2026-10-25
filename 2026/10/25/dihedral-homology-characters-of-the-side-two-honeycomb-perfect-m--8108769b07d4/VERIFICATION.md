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

# Reproduction and limits

Execute `python3 verify.py` with the standard Python 3 library. No network, external data, or packages are used.

The script reconstructs the 24 elementary triangles in the side-two regular triangular-lattice hexagon and its 30-edge dual, enumerates exactly 20 perfect matchings by recursively pairing the least unmatched triangle with every available neighbor, then builds the full simplicial complex as their downward closure (66,370 faces, counting the empty face).

An explicit 30-stage toggle matching pairs 66,368 faces into 33,184 covering pairs and leaves two dimension-three faces. The script constructs all directed Hasse cover relations with matching edges reversed and completes a topological sort over all 66,370 faces. This is a finite acyclicity certificate. The discrete-Morse theorem then supplies the homotopy argument stated in RESULT.md.

For each of the 12 dihedral elements, the script verifies the edge permutation induced by the triangular lattice transformation. It computes the reduced Lefschetz character by parity of selected vertex orbits and independently computes the full signed augmented chain trace using inversions of the induced orientations on every invariant simplex, including the empty face. Both exact integer calculations agree in every case. The resulting traces are \((2,0,2,0,2,0)\) for rotations and \((0,-2,0,-2,0,-2)\) for reflected rotations.

The checks enumerate every face of this precisely specified finite complex, so they are exhaustive for this object. They do not certify publication priority, prove anything for larger honeycombs, supply integral \(\mathbb Z[D_6]\)-module structure, or constitute independent validation.
