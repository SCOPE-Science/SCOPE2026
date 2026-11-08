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

The Johnson J(6,3) graph has twenty 3-subset vertices, and closed radius-one balls N[v] of ten vertices each (1 center and 9 neighbors); the closed-ball nerve comprises subsets of one of the twenty balls, *not* the Rips clique complex. An independent fully written algorithm enumerated all 16141 augmented faces with exact f-vector, performed 6814 valid elementary simplicial collapse pairs, leaving a 2513-face core, then 1233 deterministic seed-220 toggle pairs. Across the original 16140 nonempty face-poset vertices/87800 covering incidences, the complete reversed matching Hasse digraph was acyclic. The Morse model has one 0-cell, thirteen 3-cells, 32 4-cells; the independently recomputed signed integer 13x32 boundary has 14 nonzero entries and Smith [1,1], rank two. Unimodular 3/4 cellular cancellation and Hurewicz give 11 S3 + 30 S4 integrally. Twenty distinct cardinality-ten facets make the complex pure 9-dimensional and its nonzero lower H3/H4 exclude pure shellability.

## originality

PASS

Best-of-knowledge PASS. Matsushita's complete primary closed-neighborhood paper defines precisely this construction and relates it to canonical double-cover independence complexes but does not calculate J(6,3) or force these exact multiplicities. The full published Resultary all-parameter J(n,k) radius-one Rips theorem does cover J(6,3) *as a flag clique complex* (19 S2), not the closed-neighborhood nerve. One closed ball contains pairs of Johnson vertices at mutual distance two; hence the Čech complex has nonclique faces and different homotopy. Open-neighborhood J(n,2) results also do not cover the claim.

## value

PASS

The self-complementary J(6,3) is the smallest symmetric middle-layer Johnson case where the metric Čech (common-ball) complex differs substantially from graph-clique Rips at the same radius; the mixed 3/4-sphere integral wedge and non-shellability are precise natural topology beyond generic suspension correspondence. Exact primitive Smith data distinguishes integral homotopy from face counts or mod-two Betti numbers, giving a useful radius-one Čech benchmark, despite no all-Johnson family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
