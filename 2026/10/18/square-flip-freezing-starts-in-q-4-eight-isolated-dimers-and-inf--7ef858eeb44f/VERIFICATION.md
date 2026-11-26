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

Independently checked the repaired dimensional scope and census. Any four-cycle in the cube flips each coordinate an even number of times; with distinct vertices the four steps alternate between two coordinates. Every matching is a bijection from even to odd vertices which respects Hamming adjacency, so the independent replay's checks of 2!, 4!, and 8! bijections are exhaustive for d=2,3,4. Enumerating opposite pairs in all coordinate squares generates precisely the defined reversible moves. The separate replay found the same vertex and edge counts, components, degree histogram, all-source eccentricities and 384-element cube group orbit of isolates. Its seed checks show that each displayed seed is a frozen perfect matching and all four are pairwise edge-disjoint. These checks support the general proof: the product decomposition Q_4 × Q_(d-4) yields independently chosen frozen matchings on all slices; squares with only outer directions have no matched edges, inner-only squares are frozen locally, and a mixed square needs the same inner edge in opposite-parity slices, which cross-disjointness forbids. Restricting the global matching to individual slices recovers all 2^(d-4) binary choices. The corrected minimality follows from the absence of isolates at d=2,3 and their existence at d=4; d=1 is explicitly exceptional and Q_0 has a single vertex.

## originality

PASS

The repaired distinct claim relative to the older literature is the exact square-only graph structure at Q_4 and the parity-slice construction yielding a quantitative bound in all d≥4. The older cited graph and tiling results do not contain this structure; the raw matching counts were already tabulated and carry no originality. Multiple later-dated indexed records have genuine, in one case nearly complete, mathematical overlap, including identical base states and ingredient-level coverage of the bound. They are explicitly credited rather than treated as distinct advances on the common content. No earlier occurrence of those overlapping statements was verified; no historical priority or independence is inferred from catalogue dates.

## value

PASS

The local four-cycle move is a natural connectivity rule for dimers. At the first nonvacuous dimension with freezing, the result distinguishes a single mobile component from symmetry-equivalent frozen states and gives exact travel distances within the mobile component. Those exact local quantities cannot be read off the raw perfect-matching total or larger-cycle connectivity theorems. The disjoint-seed construction additionally certifies a doubly exponential family of isolated states in arbitrary dimension rather than an incidental small census alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
