---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Represent M_{2n} as twisted n-column two-rail ladder. For n≥4 all four-cycles are the n canonical rung/horizontal faces. Every perfect matching with at least one rung splits into even-length rung-free runs tiled uniquely by horizontal pairs, corresponding bijectively to an independent set of the cyclic n-edge index graph. The only rung-free matchings alternate along the 2n boundary; for even n they are the two maximal alternating independent sets, for odd n they are two extra frozen matchings with no completed square. Four-cycle switches precisely insert or delete a legal independent-set coordinate. Deleting S\T then adding T\S proves switch distance |S△T|; maximal distance 2⌊n/2⌋. Independence-set enumeration gives Lucas L_n vertices and nF_(n−1) edges. Independently built exact 2n-vertex graph, brute-enumerated all perfect matchings and four-cycles for n=4..10, found components [Λ_n] if even and [1,1,Λ_n] if odd, and reproduced edge counts. The all-n theorem uses the forced tiling proof, not finite enumeration.

## originality

PASS

Targeted statement/implication comparison against related published Resultary research records and primary sources; best-of-knowledge originality with explicit risks. For every Möbius ladder M_{2n}, n≥4, its local four-cycle perfect-matching flip graph is Lucas cube Λ_n for even n and Λ_n plus two isolated vertices for odd n, with exact distance, matchings, edge counts.

## value

PASS

The four-cycle switch graph is the natural local dynamics of matchings/dimer configurations. An exact all-width graph isomorphism to the Lucas cube yields exact reachability, Hamming distances and a parity-driven frozen sector, none of which follows from the previously known scalar matching count alone. This is a natural structural classification rather than arbitrary numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
