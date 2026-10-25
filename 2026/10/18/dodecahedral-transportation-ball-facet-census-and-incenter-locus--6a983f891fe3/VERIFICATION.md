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

The canonical GP(10,2) graph yields the symmetric edge polytope of dimension 19; polarity identifies facet normals with integer 1-Lipschitz functions modulo constants whose saturated-edge graph is connected. The tight connected graph must have a spanning tree, proving integrality, so rooted recursive assignment over all legal adjacent intervals exhausts the search. Independently compiled and executed a separate C++ enumerator based on the inspected graph: 14,607,387 normalized integral 1-Lipschitz profiles, 3,678,208 tight-connected facets with histogram (19:411840,20:934968,21:1103600,22:801000,23:352440,24:74360); the maximum T=20 sum f^2-(sum f)^2 is 580 at exactly 20 potentials. Independent distance BFS found layers 1,3,6,6,3,1 and center-normal span rank10, with explicit 10x10 determinant -2. Distance profiles have squared centered norm29 giving origin inradius 1/sqrt29 and 20 contacts; central symmetry proves global maximality and slack for other facets gives a local relative neighborhood of optimal centers in the rank-10 annihilator, hence affine dimension9. Entire arithmetic is finite and exhaustive because graph and integer-assignment completeness were proved; no claim about other Euclidean embeddings.

## originality

PASS

Best-of-knowledge originality PASS after fresh published findings search and mathematical comparison of alias objects, stronger coverage, exact tables, and prior-result implications. Known general tools are credited, rather than claimed anew; risk remains documented: An unindexed previously published dodecahedral symmetric-edge-polytope database or computational facet table may contain the exact numbers; external exhaustive priority check not possible.

## value

PASS

The dodecahedron is a canonical vertex-transitive graph. A complete 3.7-million-facet census with exact facet incidences, tangent normals and a nine-dimensional (nonunique) maximal incenter locus is a substantial exact invariant of its 19-dimensional transportation polytope; the large exhaustive classification and center geometry are usable fixed-object benchmarks, not an arbitrary small slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
