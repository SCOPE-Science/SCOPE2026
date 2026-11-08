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

For G_n=K_n square K_2 under synchronous 3-state threshold-one Greenberg--Hastings update, every matched pair has one of nine ordered types (a,b); its successor depends only on whether any left or right type contains state 1. Occupied-type support therefore determines all iterates for every n. The 511 nonempty supports are exhaustively checked with exact symbolic transition; F^16=F^4, least eventual periods 1,3,4, entry <=4, and the nine-row by-period support table. Inclusion-exclusion surjections U_j(n) produce B1=3*4^n+6*3^n-12*2^n+3, B3=9^n-9*4^n+18*2^n-9, B4=6*(4^n-3^n-2^n+1); four-step bound is sharp. Counting recurrent support classes and three-coloring criterion gives C4=2^n-2 (known) and stated C3. Independent nine-type support computation checked all 511 supports and direct vertexwise dynamics 7371 labelled states n=2,3,4; these corroborate a genuinely exhaustive finite 9-type reduction, not merely small-n extrapolation.

## originality

PASS

Best-of-knowledge scoped originality after explicit implication comparisons, with real residual priority risk: Full comparison with all unindexed specific rook-graph GHCA basin tables remains incomplete; the 511-support reduction is proof-critical and relies on exact original pair update, which was independently reproduced. Period-four count is known rather than novel.

## value

PASS

A complete all-initial-state attractor-period partition and sharp bounded transient on the canonical matched-clique excitable network, including an exact probability that period-three attraction tends exponentially to one. This is a natural dynamical census not obtainable from merely knowing periods or a prior four-cycle count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
