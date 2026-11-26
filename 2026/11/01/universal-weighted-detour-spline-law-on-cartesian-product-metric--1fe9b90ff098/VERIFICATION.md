---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The ambient metric bounds every skeleton route below by its sum of factor distances. For different moving coordinates, perform the initial coordinate's move to the target vertex first, the vertex-to-vertex moves next, and the move into the terminal interior last. For different underlying edges in the same moving coordinate, a factor shortest path must pass through a vertex, where all other moves can be inserted. On a single edge copy the direct subsegment is shortest: otherwise the factor edge's endpoints could be joined by a shorter route. For two distinct copies of the same geodesic edge of length ℓ, a route must project in the moving coordinate through a departure endpoint and an arrival endpoint. A common endpoint gives the horizontal lower bound s+t or 2ℓ−s−t (attainable while making all other moves there); opposite endpoints require at least ℓ in that projection, no better than the smaller common-endpoint cost. The other projections require their layer distance. Thus the detour is twice the minimum of the four distances of the two arclength positions from the endpoints. For z≥0 it exceeds z exactly when both coordinates are in (z/2,ℓ−z/2), with area (ℓ−z)_+². The b_i(b_i−1) ordered copy pairs, each of mass ℓ²/Λ², give the survival law; vertices are null. Integrating q z^{q−1} against the survival for q>0 yields the stated moment, and the scaled conditional survival is (1−z)² on [0,1]. The positive weights make the downward jumps of the one-sided second derivatives at all positive lengths identifiable. Finally, conditional on a distinct copy pair, at a threshold within x∈[0,ℓ] of the layer distance the ambient horizontal CDF is 2x/ℓ−(x/ℓ)² and the intrinsic horizontal CDF is (x/ℓ)² by two planar triangle area computations. Their difference is zero at the endpoints and elsewhere outside that interval; weighting recovers the exact correction and its strictness condition.

## originality

PASS

The distinct supported claim is the joint extension to arbitrary positive geodesic weights and finite numbers of factors, with the full all-threshold detour and CDF correction and an identifiable weighted length spline. The equilateral two-cycle survival, conditional Beta law, and CDF correction are direct overlaps, not new special-case claims here.

## value

PASS

The one-skeleton restriction is a natural network-routing constraint. Detecting exactly when it matters transforms a potentially full edge-pair geometric problem into a shape-independent weighted spline; the correction retains layer-distance data and the derivative jumps recover the weighted aggregate length spectrum. For instance, two three-vertex path factors with edge lengths (1,1) and (2,2) have the same detour law and Λ as factors with (1,2) and (1,2); the theorem recovers the aggregate but cannot distinguish those allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
