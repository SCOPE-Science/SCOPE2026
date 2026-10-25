---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

With outside-vertex open-neighborhood traces, a graph non-star LD set is exactly a vertex cover of H, where H has cliques on each nonsingleton part and a clique on singleton-part vertices. Both directions hold because covers select vertices from at least two distinct parts, hence all outside traces nonempty and distinguishable. A coalition partition induces a looped quotient graph J on blocks: no singleton vertex cover, every index in at least one size-two vertex cover. In such a graph at most four indices can appear: two disjoint constraints force at most four possible endpoints, while no disjoint edges and no one-cover force a triangle, at most three. Four blocks rule out triangle cliques and require H to be a matching with two or more edges; explicit cross-pair construction gives four. Twin-pair plus remainder yields three, with stars handled by direct LD minimum m and pairwise coalition bound. Formula C_L=4 iff max part<=2, singleton count<=2 and (#2-parts)+1_{#singleton=2}>=2; otherwise 3, for r>=2 and N>=3. Independently exhaustively enumerated all LD subsets and all set partitions for 36 part-size profiles N3..7; every case matched. Inspected actual verifier for larger n and graph-lemma check; finite tests corroborate unrestricted proof.

## originality

PASS

Chellali et al. 2026 introduce the parameter, give C_L<=N-gamma_L+2 and general small cases, not the all-size multipartite formula. Its 23-page primary PDF was inspected including general bound, paths/cycles and small-order regimes. The published Resultary self/solid locating-domination on complete multipartite graphs uses different conditions and does not count coalitions; other (3,2)-domination variants likewise not implications. Specific small graphs already covered by old theorem are credited, not the main infinite classification.

## value

PASS

A recently defined coalition parameter has general order-dependent estimates; the complete structural classification on the natural and unbounded complete multipartite family gives a sharp absolute 3/4 dichotomy and explicit extremal partitions, with the vertex-cover quotient explaining why four is maximal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
