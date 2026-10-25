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

Reproduce the finite checks from the embedded standalone script `verify_icosahedron.py` using Python 3 with NumPy and NetworkX:

```bash
python verify_icosahedron.py
```

The executed script reconstructs a normalized twelve-vertex regular icosahedron and its thirty graph edges, twenty triangular faces and six antipodal axes; enumerates all 120 automorphisms; reconstructs the corresponding orthogonal geometric actions and signed six-axis permutation matrices; and checks the geometric three-plane projection and the invariance of the complementary three-plane. It also enumerates the complete 164-subgroup lattice and checks fixed-dimension doubling. Recorded completion lines:

```text
ICOSAHEDRAL_GRAPH_AND_ACTION_VERIFIED 120 20 6 {1: 60, -1: 60}
CANONICAL_EQUIVARIANT_THREE_PLUS_THREE_SPLITTING_VERIFIED
PROJECTION_NONZERO_ON_ALL_TWENTY_FACE_SIMPLICES_VERIFIED
ALL_SUBGROUP_FIXED_DIMENSION_DOUBLING_VERIFIED 164 [(0, 86), (1, 62), (2, 15), (3, 1)]
```

The source of the general result is the written proof: exact cross-polytope structure, positive face-supporting halfspaces, the equivariant orthogonal-projection homotopy, and Galois-conjugate character averages for arbitrary subgroups. The numerical program uses tolerance-based floating-point coordinates and finite enumerations. Its success alone would neither certify exact arithmetic nor establish the claimed homotopies. The claim does not require enumeration of arbitrarily large objects: all groups involved are finite subgroups of the explicitly determined 120-element symmetry group.

Independent mathematical audit: not performed.
