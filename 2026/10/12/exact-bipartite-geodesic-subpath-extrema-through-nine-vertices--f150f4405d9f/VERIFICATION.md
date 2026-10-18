---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Independently coded BFS shortest-path multiplicities on all two-shore binary incidence masks for each n=7,8,9; all 2^20 four-by-five masks included and connectivity checked, not sampling. Reproduced maxima 49/74/105 and fixed-shore labeled profiles n7 {0 missing:1, one missing:12}, n8 {one missing:16, deleted disjoint 2-matching:72}, n9 {deleted 2-matching:120, 3-matching:240, 2 disjoint K1,2 stars:60}. All shore splits produced smaller maxima. BFS recurrence counts each geodesic exactly and includes n zero-length paths. Both original BFS/Floyd C++ source algorithms inspected for exhaustive bounds; independent program verifies table.

## originality

PASS

Natural exact global finite first orders solving a portion of Knor et al. Problem 15, not implied by subfamily bounds. A new diameter-four two-disjoint-star coextremizer is outside prior matching-deletion results.

## value

PASS

First complete finite exact equality layer for a published open bipartite extremal problem; small n are mathematically motivated thresholds and one 9-vertex diameter-four graph defeats a natural matching-only ansatz. Provides reproducible nontrivial global finite benchmark, not a generic table without purpose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
