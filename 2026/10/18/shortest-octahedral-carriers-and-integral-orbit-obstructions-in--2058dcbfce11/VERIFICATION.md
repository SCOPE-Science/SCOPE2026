---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The graph GP(6,2) has twelve vertices, eighteen explicitly ordered outer-cycle/spoke/inner-triangle edges. The ordinary matching complex on those edges has f-vector (18,117,334,402,156,10), independently reconstructed. Its flag property gives an eight-vertex minimum support for nonzero H3 and forces equality supports to be octahedral (S0)^{*4}; these are exactly four disjoint two-edge paths spanning all twelve vertices. Independent full enumeration found precisely 93 carriers from 36 local incident-edge pairs. The provided complete 1037-face deterministic vertex-toggle discrete Morse matching has 507 pairs and critical faces one vertex plus 22 tetrahedral faces. Independently constructed every Hasse incidence and verified the matching is acyclic, so the Morse CW complex proves the wedge of 22 copies S3 (not merely rational homology). The inspected exact integer cancellation projects all 93 oriented 16-facet join cycles onto a 22-dimensional integral Morse lattice; each coordinate vector is primitive, a chosen 22 have signed determinant +1, establishing integral generation. Under the 12-element D6 action, carriers split into eleven orbits of lengths (6,12,6,3,12,12,12,12,6,6,6), with individual ranks (5,8,6,3,12,12,9,8,6,6,6) from exact normal forms. Among 165 3-orbit combinations, source integer Hermite/Smith reduction gives exactly 26 rational full-rank, of which 23 index1 and 3 index4, exceptional triples (2,4,10),(2,5,7),(2,5,10), each quotient (Z/2)^2; no two-orbit combination spans. An independent modular recomputation matched boundary ranks at primes 2,3,5,101, rank22 spanning by all carriers, 26 full-rank triples mod101 and exactly 23 mod2 with precisely these three parity exceptions. Integral group type (2,2) depends on source integer Smith reduction, not on modular checks alone.

## originality

PASS

Bayer–Jelić Milutinović–Vega prove a wedge for outerplanar underlying graphs, but GP(6,2) is nonouterplanar (independently checked), and an abstract wedge alone cannot entail shortest carriers or integral orbit cokernels. Zhao studies perfect-matching forcing-polynomial counts on GP(n,2), not matching-complex homology. The closest indexed index-four parity calculation for a Möbius ladder uses a different inclusion map and graph. Here the exact 93-carrier D6-orbit lattice, especially three noncyclic index-four obstructions, is not a trivial corollary of known wedge/homology results.

## value

PASS

The Dürer graph is a canonical small generalized Petersen graph with nontrivial symmetry. Its complete finite induced-shortest-sphere census and the distinction between rational spanning and integral saturation of symmetry-orbit classes give a precise topological-arithmetic obstruction; the three (Z/2)^2 parity failures are meaningful information that ordinary ranks miss. This is a motivated natural finite classification, not an arbitrary parametric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
