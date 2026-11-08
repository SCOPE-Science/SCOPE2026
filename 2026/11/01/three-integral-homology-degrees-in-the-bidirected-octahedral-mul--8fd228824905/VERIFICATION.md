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

The graph is exactly bidirected K_{2,2,2} on six vertices with 24 arcs, and valid multipaths are injective partial successor maps with no directed cycles. Independently exhaustive arc-subset enumeration gives 1817 augmented faces, f-vector (24,192,616,744,240) and maximal facet distribution 240 in dimension4 plus 24 in dimension3. Two independent face enumeration models agree. An independent Forman matching processes arcs in lexicographic order and yields 835 pairs leaving critical cells 1 in d0,12 in d2,101 in d3,32 in d4; full reversed-Hasse DAG on 1816 nonempty faces and 6408 incidences is acyclic. Independently regenerated signed gradient-path Morse matrices give ∂3 of size12×101 with 257 nonzeros and SNF nine unit invariant factors, and ∂4 of size101×32 identically zero; original simplicial GF2 boundary ranks (23,169,444,208) corroborate. Integral homology is H~2=Z³,H~3=Z⁹²,H~4=Z³², zero otherwise, with no torsion. A CW model with one zero-cell and no one-cell is simply connected; Hurewicz gives π2=Z³. No unproved sphere-wedge assertion was inferred.

## originality

PASS

PASS best of knowledge: multipath-complex theorem families for bidirectional paths/cycles and different orientations do not determine the six-vertex bidirected complete-tripartite octahedron integral groups. Exact chain calculation and π2 are not a known-table recomputation in inspected sources.

## value

PASS

Bidirected complete-tripartite graphs are a natural first multipartite extension beyond published bidirectional paths and cycles, and K2,2,2 is the standard octahedral smallest balanced instance. Its three mixed homology degrees, exact integral torsion-freeness and first nonzero π2 show structural behavior hidden by rational Euler counts. The complete exact result is a reusable concrete invariant and test case for multipath topology, even without a broad classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
