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

For every integer n≥4, M_(2n) is the graph on Z/(2n) with rim edges {i,i+1} and antipodal spokes {i,i+n}; ordinary Δ3 facets complement *disconnected* triples, not independent triples. Its Alexander dual L contains all vertices/edges and the 6n connected induced P3-triples (2n rim R_j and 4n mixed) as triangles. In a triangle-free induced 4-set, requiring all triples connected forces four edges and hence a 4-cycle; M_(2n) has precisely n spoke-rim squares Q_i. No five-set can belong to L: ten connected triples require ≥20 edge incidences but each graph edge participates in only three triples and a five-vertex triangle-free graph has ≤6 edges, giving ≤18 incidences. Explicit 6n elementary collapses: first n pairs (Q_i,abc), then 2n pairs (R_j,{j,j+2}), then 3n pairs (bcd,bc),(abd,ab),(acd,ad), with (a,b,c,d)=(i,i+1,i+n,i+n+1). Each lower face is free from the exact square/chord incidences and prior removal order, including overlapping spokes; no other 2- or 3-faces survive. Graph remaining has 2n vertices, C(2n,2)−5n edges, and is connected via selected rim segment n,n+1,...,2n−1,0 plus n antipodal spokes, hence L≃wedge^(2n²−8n+1) S1 integrally. Duality gives Δ3 reduced integral homology only in degree 2n−4 with that free rank. Since L has no five-vertex face, Δ3 has full (2n−6)-skeleton, hence is simply connected for n≥4; successive Hurewicz and homology Whitehead yield Δ3≃wedge^(2n²−8n+1) S^(2n−4). Independent implementation (not reliance on VERIFY_OK) enumerated all connected triples, all 4-faces, every proposed free-face collapse, residual-graph connectivity and Betti count for n=4,5,6,7,8,12; additionally all ordinary-cut faces and direct mod-2 chain Betti ranks for n=4,5,6. All matched β=1,11,25,43,65,193 for listed n and mod2 sole β in degrees 4,6,8 at smallest cases. Finite replay corroborates but does not replace uniform proof; integral torsion-freeness comes from simplicial collapses, not mod2.

## originality

PASS

Qualified best-of-knowledge original infinite-family homotopy classification for **ordinary** Δ3 of Möbius ladders M_(2n) (n≥4). Actual Resultary queries compared equivalent circular ladder rank, stronger triangle-free edge-disjoint-square and high-girth results, and the same-graph total three-cut theorem by exact object, assumptions and implications. Direct full-result text inspections establish that the first concerns nonisomorphic untwisted prism graphs, the next two have violated square/girth hypotheses, and the last has a distinct facet definition and degree. Foundational cut-complex papers and circular-prism conjecture do not yield this twisted family from inspected statements. The very relevant Agarwal–Basak same-graph manuscript had accessible abstract only: arXiv/OA full text failed, Oxford reported VPN disconnected; this is a specific priority risk, not automatic failure nor a whole-paper exclusion. Unindexed equivalent results remain possible.

## value

PASS

An infinite-family integral homotopy classification for the natural 3-regular Möbius ladders under the established ordinary three-cut functor, with exact dimension and sphere multiplicity, contributes a motivated structural result, not a routine textbook deduction or arbitrary finite case. Antipodal twist changes topology of the graph and invalidates a naive transfer from circular prisms and overlapping square incidence invalidates a previously known broad theorem. New uniform exact 6n elementary simplicial collapses prove torsion exclusion, and the n=4 Wagner boundary is included. The object and exact invariant are canonical in cut-complex topology, and are directly useful for understanding twist sensitivity, expected cut-complex homotopy and related graph families. No claimed total-cut, equivariant, shellability or general graph result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
