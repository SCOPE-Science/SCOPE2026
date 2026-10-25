---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Enumerating all 2^16 vertex subsets identifies 321 independent faces including the empty simplex, 80 4-facets and a complete explicit 80-facet shelling order (3160 prior-facet comparisons in inspected certificate). Shelling implies X and links of all faces are wedges of spheres in top degree with torsion-free integral homology; the Euler characteristic gives exactly one S3. Independently implemented combinatorial orbit and bitset mod-2 boundary-rank computations on all 321 faces confirm 17 dihedral face orbits and top-link rank 2 on vertices, edge distance 2/5/7 and one 32-triangle orbit, rank 1 elsewhere. Original checker also verifies mod3; shellability supplies integral torsion freeness, not inference from two primes alone. Rank-two triangles have 16 vertices,48 edges,32 triangles, each edge in two triangles, each vertex link a connected six-cycle; explicit oriented 32-triangle chain has zero integer boundary and chi=0, giving a connected orientable torus. The local-homology shift matches top H3.

## originality

PASS

Original Earl–Vander Meulen–Van Tuyl 2015 Theorem 6.1 establishes shellability but not vertex decomposability of exactly C16(1,4,8), and prints a shelling. That known component is fully credited. No classification of local homology ranks or embedded toroidal entire rank-two locus appears in its inspected theorem/proof; related lexicographic-product paper addresses shellability rather than the exact singular torus. Resultary hits concern distinct independence complexes and circulant torsion cases.

## value

PASS

A natural explicit finite obstruction illustrating that shellable flag S3-homotopy type does not imply integral homology manifold, with complete local homology and nontrivial two-dimensional toroidal singular locus. Exact topology rather than merely recomputing an old shelling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
