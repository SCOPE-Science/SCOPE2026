---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. The object is the ordinary matching complex of the labeled Pappus cubic graph with LCF [5,7,-7,7,-7,-5]^3, not an independence complex or a perfect-matching subcomplex. Reconstructed the 27 graph edges and all 35,368 matchings including the empty one. Independent exhaustive F2 boundary elimination gave augmented ranks (1,26,271,1448,4195,6362,4335,984,42) and only reduced mod-2 Betti 40 in degree 5, bounding rational homology there; the signed Euler characteristic agrees. Reconstructed all 216 graph automorphisms by adjacency-preserving bijections, independently evaluated the fixed matching-orbit Lefschetz formula on every automorphism, and reproduced eleven vertex/edge cycle profiles and character distribution (-4:18,-2:36,-1:36,0:81,1:12,4:32,40:1). The original verifier also implements independent direct signed simplex traces. The character sum is zero and rational invariants, hence positive-degree rational homology of the finite orbit quotient, vanish. This is a complete finite exact character, not a homotopy classification of the quotient.

## originality

PASS

PASS on checked primary implications. Same Pappus matching complex has a prior integral wedge of forty 5-spheres and earlier mod-2 Betti vector, but these nonequivariant statements do not determine action of the complete order-216 graph-automorphism group on rational homology. Searches for a matching complete 216-element character/table and symmetry quotient did not find one; related Heawood and cycle-matching equivariant results have different graph objects. A missed unindexed character calculation remains possible.

## value

PASS

PASS. The Pappus graph is a canonical symmetric cubic incidence graph and its ordinary matching complex already has interesting nontrivial fifth homology; determining the full natural automorphism module is a motivated missing invariant rather than an arbitrary small slice. The complete character separates eleven group-cycle profiles, discovers no globally fixed rational cycle and computes the quotient homology. It refines a known natural 40-sphere homotopy classification with significant structure; finite exact computation is appropriate for this fixed graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
