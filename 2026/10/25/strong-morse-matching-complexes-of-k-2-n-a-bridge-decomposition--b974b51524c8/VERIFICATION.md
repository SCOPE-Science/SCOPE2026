---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each total order of K_(2,n), a graph vertex produces a strong matching exactly when it has one earlier neighbor. Inspecting the positions of the two high-degree vertices exhausts all matching facets: two disjoint complexes D_a,D_b, each a central (n−1)-simplex with n attached ridge simplices, and 3n maximal cross-component edges. Every facet has an explicit realizing order. Each D_i admits an explicit S_n-equivariant deformation retract to its central simplex, so contracting both yields a two-node multigraph with 3n edges and integral wedge of 3n−1 circles. Relative H1 exact sequence is ker(sum:(Z^n)^3→Z) and rational trace 3 Fix(σ)−1. Face vector f_(r−1)=2[C(n,r)+nC(n−1,r−1)]+3n·1_(r=2). Independent enumeration of all (n+2)! orders for n=3,4,5 reconstructed all matching sets and exact facet/face model (face vectors (12,27,8),(16,48,32,10),(20,75,80,50,12)).

## originality

PASS

The 2026 founding primary explicitly computes full strong complexes for paths, stars, simplices, boundaries, and finite-range cycle cases, NOT this complete bipartite variable family; ordinary Morse matching complex on the same K_(2,n) is a DIFFERENT simplicial object. The bridge homotopy decomposition and integral S_n-module consequently survive as best-of-knowledge new.

## value

PASS

This natural infinite graph family has complexes with maximal faces of dimension n−1 but homotopy concentrated in degree one. The two-contractible-piece/3n-bridge explanation and exact integral permutation representation are nontrivial structural data beyond low-n computations and beyond Betti ranks alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
