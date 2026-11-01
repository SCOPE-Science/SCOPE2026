---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Every polygon is the hull of some subset of the sixteen integer grid sites; monotone-chain integer determinant hull extraction deduplicates all subsets. The convex normal fan partitions objective directions by primitive edge-normal rays and open sectors, whose directed adjacency is constant. Exact integer shortest increasing-path DP on each direction is exhaustive. Independent enumeration found 2719 unique hulls, all seven (vertex-count, diameter) strata 516,1038,648,200,292,24,1; unique H eight vertices and diameter 4; checked all nongeneric rays. This is a genuine *finite exhaustive proof*, not an extrapolation.

## originality

PASS

Black 2026 gives high-dimensional exponential examples for [0,3] grid boxes and Black 2022 treats [0,2] grid bounds, while Chadder–Deza address undirected graph diameter. None of these implies the 2719-polygon exact planar three-grid table. A prior exhaustive table or online database is a residual risk.

## value

PASS

The three-grid is a distinguished threshold setting in lattice-polytope monotone diameter research; an exact natural small-dimension classification, sharp extremum and unique geometric witness offer useful benchmark data beyond arbitrary small-instance computational noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
