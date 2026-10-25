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

## Mathematical checks
The claim concerns geometric fixed points for a fixed order-two translation by a weight-three vector in a hypercube; it is not a theorem about individually fixed vertices (there are none). With \(m=n-3\), the invariant simplicial orbit complex is built from four color-classes over each vertex of the cube graph \(Q_m\). Distinct orbit vertices over a common cube vertex are pairwise compatible; vertices over adjacent cube vertices are compatible exactly for different colors. Since a cube graph is triangle-free, all maximal faces live over its edges, forming boundaries of four-dimensional cross-polytopes. They glue along tetrahedral facets. The spanning-tree and non-tree-edge homotopy-pushout steps give exactly \(e\) copies of \(S^3\) and \(e-v+1\) circles for every \(m\ge1\).

## Computation
Run `python verify_weight3.py` with Python 3 (standard library only). The program directly computes compatibility from Hamming distances of antipodal pairs, exhaustively enumerates maximal cliques with `standalone bitset Bron–Kerbosch clique enumeration`, verifies they coincide with the claimed cross-polytope facets, constructs every simplicial face, and independently calculates mod-two chain ranks. The tested cases \(n=4,5,6,7\) yielded reduced Betti vectors (in degrees zero through three): \((0,0,0,1)\), \((0,1,0,4)\), \((0,5,0,12)\), \((0,17,0,32)\). The final executable marker is `WEIGHT3_TRANSLATION_FIXED_COMPLEX_VERIFIED`.

## Unproved scope
Finite checks alone do not establish a universal homotopy type or integral torsion-freeness. The proof uses genuine homotopy-pushout splittings, not extrapolation of the mod-two rank experiments. Only a weight-three translation, not arbitrary automorphisms or other scales, is covered. Independent audit: not performed.
