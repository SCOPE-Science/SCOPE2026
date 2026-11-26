---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently counted the binary adjacency kernel using each petal's internal equations z_{j+1}=z_{j−1}, with z₀=z_ℓ equal to the common hub coordinate. Even positions have the hub value and odd positions have one free candidate value per petal. Closing an odd petal forces its candidate to equal the hub; closing an even petal leaves it free. The two terms in the hub equation from each petal agree and cancel. Nullity is therefore 1 plus the number of even petals, which gives rank 2s. For a size-s cover, A=MJMᵀ and rank forces the side-incidence matrix M to be injective; Eulerian parity gives A1=0 and thus Mᵀ1=0. Every side is even and hence so is the XOR edge count; odd o is impossible at rank equality. For the upper bound checked the paired triangles explicitly: the two K₂,₂s share only the extra cross-edge bc; the other six edges are exactly the two triangles at the hub. A square costs one biclique and an unmatched triangle costs two. A rim-edge replacement uv→uxyv toggles only uv, ux, xy, yv by one K₂,₂ on disjoint sides {u,y} and {x,v}. This preserves all other edges regardless of previously used cancelling edges, and generates every length with one biclique per two added vertices. The total is s+(o mod 2), including t=1 and o=0. The uploaded checker was inspected, not run; its finite tests and exact-small-instance search are corroboration only.

## originality

PASS

Credit prior single-cycle values, the rank and even-core lower bounds, and the butterfly example. The supported distinct result is the uniform rank and matching upper/lower formula for one-vertex unions, where the gap depends on parity of the number of odd petals. The comparison is limited to inspected sources; it does not claim priority for the known ingredients.

## value

PASS

Cycle bouquets are a natural first articulation family after disjoint cycles. Their exact gap above half the binary rank changes from a presence-of-odd-cycles criterion to an odd-number criterion. This isolates what hub identification permits—pairing odd petals by cancelling a cross-edge—and yields an optimal constructive answer for all petal lengths rather than a small example or enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
