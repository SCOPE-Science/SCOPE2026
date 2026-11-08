---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Exact finite claim for GP(10,2): define outer cycle u_i u_(i+1), spokes u_i v_i, inner v_i v_(i+2), each for i mod 10. Vertex OCT means remaining induced graph bipartite. Independently implemented exact enumeration in a newly written standard-library program that tested all 60,460 subsets of 20 vertices of sizes 0..6 (zero feasible below six, exactly 3240 at six), constructed all feasible one-removal/one-addition arcs and all-pairs BFS. Independently obtained 31800 undirected exchange edges, degree histogram (12:150,14:480,15:240,16:30,17:240,18:120,19:120,20:240,21:480,22:120,23:240,24:260,25:360,26:120,27:40), eccentricity 6 for every one of 3240 states, and exactly all 10 metric table entries including 67,480 (ordered) excess pairs. Every BFS reached all 3240 states, and every counted pair satisfied h <= d <= h+1; strict cases exist. Independently checked the nonmatroid witness {1,5,7,9,11,14}, {6,9,10,12,13,15}: both feasible, replacing 5 by any vertex of T\S fails. Inspected both repository verifier algorithms (including checked GP-to-LCF isomorphism) and both output JSON files. Actual frozen source Git tree reconstructed independently from all ten listed file blob identities and matched 92d25604fcaaf3a6f5b86560ed0c6f75e0799f03. Complete exhaustive finite computation is a proof for this fixed graph and all its allowed states, not an infinite-family extrapolation.

## originality

PASS

Qualified best-of-knowledge originality for the full constrained optimum-solution graph metric (3240 six-vertex OCTs, 31800 swap edges, one-detour Johnson bound, exact pair table and 33740 exceptional unordered pairs), not the known scalar dodecahedral bipartization number, basic token-jumping definition, exhaustive-search method or ambient Johnson lower bound. Fresh Resultary searches and primary scientific comparisons found no theorem/table logically entailing these exact constrained distances. Importantly the once-inaccessible closest Zhu manuscript was found as an author-hosted full PDF and materially inspected this run: it treats maximum induced-bipartite cardinalities and the exceptional dodecahedron, NOT the optimum-solution reconfiguration metric. Novelty is best knowledge with historical table risk, not formal priority certification.

## value

PASS

The dodecahedron is a canonical exceptional cubic fullerene for bipartite induced-subgraph bounds. Maximum induced bipartite subgraphs and their optimum-preserving vertex exchanges form a natural optimization reconfiguration object: feasibility can constrain paths substantially beyond the Johnson lower bound. A complete exact 3240-state metric, self-centered nonregular structure, sharp one-step detour bound with exact 33740 unordered obstructions, and a specific violation of matroid basis-exchange characterize the geometry of all optimal solutions rather than simply recomputing the known scalar optimum of six. This is mathematically motivated and could serve as a natural exact benchmark for feasible-solution reconfiguration, without requiring an all-fullerene generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
