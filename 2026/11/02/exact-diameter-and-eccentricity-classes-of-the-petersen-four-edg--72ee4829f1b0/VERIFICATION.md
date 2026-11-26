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

An independent exhaustive reconstruction used fixed-order edge assignments with endpoint masks, built each two-colour component by traversal on the ten Petersen vertices, and checked that every resulting neighbour was a proper enumerated state and every adjacency was reciprocal and loop-free. The graph automorphism group is exactly S5: the five size-four independent sets of KG(5,2) are the five stars of two-subsets through a fixed symbol. A pairwise intersecting family of two-subsets without a common symbol has size at most three; each vertex is recovered as the intersection of its two stars. Applying adjacent transpositions on symbols and on labels therefore gives the full required orbit decomposition. One complete BFS per orbit independently gave 49,920 states, 377,280 edges, degrees 15 and 16 with multiplicities 44,160 and 5,760, 21 orbits, radius 7, diameter 8 and eccentricity multiplicities 45,600 and 4,320. BFS reached all states. The two eccentricity-eight orbit sizes and far-sphere sizes gave (1440*2+2880*1)/2=2880 unordered pairs. The replay matched every frozen representative to a different reconstructed orbit, verified every sphere vector and recovered the exact recorded far targets at both eccentricity-eight roots, including the stated witness.

## originality

PASS

The count and connectivity are already known and are correctly credited. The strongest inspected tables and reconfiguration results do not supply the claimed local degree, combined symmetry-orbit, eccentricity or distance-eight classification. This assessment applies to those additional data, not to the state count or connectivity.

## value

PASS

The Petersen graph is a canonical class-two cubic graph and four is its smallest feasible palette. For the natural component-switch move, exact distances quantify the worst-case number of exchanges and distinguish typical states from the peripheral ones, information not given by connectedness. Counting the extremal pairs and classifying their two orbit types provides a concrete benchmark for reconfiguration and symmetry-reduction methods rather than another computation of the previously known state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
