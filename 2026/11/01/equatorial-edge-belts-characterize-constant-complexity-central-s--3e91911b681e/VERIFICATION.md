---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For a generic central normal u, every section vertex is exactly one polytope edge whose endpoint signs are opposite. Crossing the great circle u·v=0 for vertex v and its antipode -v changes this count by -2 times the neighbor-sign imbalance at v. If the count is constant, this sign sum must vanish for all generic u in v^perp. The planar sign-jump lemma implies that the nonzero projected neighbor directions at v occur in antipodal pairs, with multiplicity. Each original edge spans a unique origin plane H, and local pairing gives degree exactly two for the polytope-edge subgraph inside H; convexity of the polygon P∩H means any such edge cycle must cover its entire polygon boundary, yielding disjoint equatorial belts partitioning every edge. Conversely a generic central plane crosses the boundary of each centered belt polygon at exactly two genuine polytope edges, so N_P(u)=2r for r belts. This establishes all three equivalences for every full-dimensional centrally symmetric convex 3-polytope, not merely tested examples. The assigned exact-arithmetic Python source was inspected: its Q(sqrt5) polyhedron construction checks the regular octahedron (3 square belts), cuboctahedron (4 hexagonal belts) and icosidodecahedron (6 decagonal belts) with generic normal tests. The cube witness has 4 and 6 section edges and distinguishes central sections from orthogonal shadows. Finite examples are not used as proof of the general implication.

## originality

PASS

Best-of-knowledge PASS for the iff equatorial-belt/local-sign-pairing criterion, not for known equatorial polygons. Cousaert’s full primary characterization is about constant-size orthogonal projections, not center-passing sections, and the cube is an explicit divergence. The known polyhedral slice-arrangement framework counts edge crossings but does not itself give the global local-pairing iff theorem. Plausibly related Birkemeyer et al. 2026 full text was inaccessible; name that residual risk without treating access alone as scientific failure.

## value

PASS

A structural iff theorem reduces infinitely many generic section directions to finitely checkable local antipodal edge-pair conditions or planar equatorial edge cycles. It explains fixed 6/8/12 side counts of three canonical symmetric polytopes and cleanly separates centered slice complexity from projection equiprojectivity. This is a motivated classification relevant to combinatorial tomography rather than a computation of familiar examples alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
