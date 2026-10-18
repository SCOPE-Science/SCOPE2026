---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

PASS. For real M=A∪B with m,n≥2, cross distances 1, within-part t∈[1,2], the base-point-normalized dual Lip ball is full-dimensional. A feasible potential is a vertex iff its tight-edge graph spans, by the full-rank incidence/midpoint/slack criterion. For 1<t<2, osc_A=t forces A to consist precisely of both L and L+t and B to lie at L+t−1 or L+1; any intermediate point is isolated. This gives (2^m−2)2^n vertices, plus the disjoint symmetric B-saturated family (2^n−2)2^m. Without internal tight pairs, even cross-edge tight paths and part diameter t<2 force both parts to be constant at levels differing by 1: precisely two vertices. At t=1 nonconstant two-level assignments give 2^(m+n)−2; at t=2 internal tight-pair saturation constrains the other part to a midpoint and gives 2^m+2^n−2. Each converse candidate has a connected tight graph. Independently wrote a half-integer grid enumerator and found exactly predicted counts for (m,n)=(2,2),(2,3), t=1,3/2,2; code in actual package verify_snowflake_biclique_vertices.py uses exact rational active-constraint intersections, inspected without executing it. These finite checks corroborate, do not prove the all-cardinality theorem.

## originality

PASS

Best-of-knowledge PASS for the strict snowflake interval and its exhaustive vertex families, not for either endpoint or the known tight-graph criterion. Compared dual Lip/Kantorovich–Rubinstein polarity, metric-snowflake and weighted graph aliases, stronger metric-polytope theory and published similarly titled findings. The cited graph results concern t=2; generic formulas assume nondegenerate metrics and do not imply this fixed nongeneric family.

## value

PASS

PASS. The full combinatorial count of supporting facets for a canonical two-level metric is a natural exact polytope invariant, and its jump from 2^N−2 to 2(2^m−1)(2^n−1) then down to 2^m+2^n−2 is not a generic face-number exercise. It quantitatively describes how snowflaking a complete bipartite graph changes the dual extremes, useful for metric-polytope combinatorics; the endpoint formulas and general tight-graph criterion receive no separate novelty credit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
