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

The vertex projection onto the opposite affine facet is its centroid. Affine linearity then gives distance hλⱼ and sends λⱼ to zero while adding λⱼ/d to every other coordinate. All projected coordinates are nonnegative, so these distances and projections really are to bounded facets. With distinct coordinates the strict order rotates as stated, with no subsequent tie. A tied block persists until maximal: each unique maximum above it moves below it, and cannot overtake the block while the latter remains unselected. Thus every weak order reaches the tied fixed set (or starts there). The arithmetic coordinate progression sums to one and rotates exactly, giving d! disjoint cycles with all phases distinct. Every complete strict-order itinerary uses each facet, and the product of their linear orthogonal projections is strictly contractive: equality would force a nonzero vector simultaneously tangent to all facets. There can be no other strict-order periodic orbit, and convergence is exponential phase by phase. Poincaré recurrence for the Borel map excludes all other points from an invariant probability, and invariance makes cycle weights uniform within each cycle. Ties have zero facet-area measure and label symmetry gives basin weights 1/d!. Independently propagating the two tetrahedral tangent vectors through j=3,2,1,0, scaling by 3 at each step, gives (0,−7,8,−1) and (0,−4,−7,11); the restricted matrix is therefore the stated matrix divided by 81, with determinant 1/81 and the claimed multipliers.

## originality

PASS

The supported distinct result is a full-boundary regular-simplex classification in d≥3, including the invariant-probability statement, relative to the established planar projection and other simplex dynamics checked. A very close separately indexed November 8 record reproduces the factorial count, arithmetic coordinates and strict/weak-order behavior on facet interiors; that portion is demonstrably overlapping and is not credited as unique. The inspected evidence does not establish preceding coverage by that record or coverage of the full-boundary statement with the invariant-probability decomposition. This is a best-of-knowledge scientific assessment, not a priority ruling.

## value

PASS

This resolves a natural, dimension-uniform regular-polytope case of Everett's higher-dimensional question, not an arbitrary parameter slice. The rank rule gives a complete division between exponential attraction and finite stopping, with an exact cycle census and a description of all stationary probabilities, including those invisible to uniform surface-area initialization. It does not claim a general result for irregular polytopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
