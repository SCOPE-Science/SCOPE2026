---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Heawood incidence graph is the 14-vertex bipartite Fano graph, (i-j) mod 7 in {0,1,3}; induced subgraph forest predicate is acyclicity and maximum internal degree d. Degree bound d=0,1,2,3 exhausts the filtration because the graph is cubic. Independently enumerated all 2^14 vertex masks using connected-component edge-count identity |E|=|V|-c, giving nonempty face counts 457,2256,8654,12791. For each d reconstructed coordinate-toggle matching and verified every oriented Hasse-cover DAG by full topological visit: cover counts 1568,10150,50764,81634, all visits equal faces; pair counts 225,1121,4326,6391; critical counts respectively {0:1,3:6}, {0:1,5:13}, {0:1,6:1}, {0:1,8:8}. Therefore genuine integral CW homotopy wedges ∨6 S3, ∨13 S5, S6, ∨8 S8, since attaching to only a 0-skeleton is null. Strict successive homology maps vanish because occupied degrees do not coincide; integral barcode is isolated intervals by stage, and stage 3 persists identically onward. No inference of integral homotopy from mere mod2 ranks.

## originality

PASS

Best-of-knowledge noncovered part: Complete integral homotopy and persistence of the Heawood forest filtration. Heawood is the smallest projective-plane incidence graph and a natural cubic girth-six test case; Novelty primarily the three new homotopy stages plus their determined persistence, and known first stage is carried only for completeness.

## value

PASS

Heawood is the smallest projective-plane incidence graph and a natural cubic girth-six test case. Giving every induced-forest degree stage as an integral wedge of spheres via explicit acyclic matchings is a natural complete classification, useful for comparison with more general incidence graphs; persistence is a faithful corollary, not falsely advertised as independent novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
