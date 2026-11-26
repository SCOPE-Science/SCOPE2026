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

In L(K_{p,q}), the selected edge ij has d(i)+d(j)−2 selected neighbors, so every nonempty component in the base graph is K_2 or a two-edge star. Counting labeled components gives the stated factorial weights: each pair of tips contributes 2!, component permutations contribute a!b!c!, and unused labels contribute u!v!. A star admits no further incident edge. Two covered endpoints on a new edge would yield two distinct selected neighbors of that new edge. If a singleton edge exists it can be extended using any unused vertex; if none exists, the only possible extension joins two unused vertices. This proves both polynomials and the EGF. The bounds s≤2p and 3s=2(p+q−u−v)−c give the maximum upper bounds; in the narrow range put h=2p−q≥1, so h has residues 0,2,1 when p+q has residues 0,1,2 respectively. The claimed maximizing b then equals h/3, (h−2)/3, (h−1)/3, with the corresponding a nonnegative since 2q−p≥p; the wide case uses p left-centered stars. The maximality branches give s=p+a or s=q+b, with the former even, and the specified star or matching constructions attain all stated minima. Comparing the extrema leaves just (2,2) and (3,4). For q≥2p, a full-coverage configuration with a singleton would force c=2p−q−3b≤0; if only the right side is required to be covered, equality forces q=2p and a=p. Thus c=u=0 for maximal sets and the stated wide polynomial, support and top coefficient follow.

## originality

PASS

Best-of-knowledge pass for the combined labeled all-set and inclusion-maximal enumeration, the exact minimum maximal size and the resulting two-exception classification. The later-dated Resultary rook record has an exactly equivalent maximal enumerator and wide spectrum; those portions are not distinct from it, and independent priority between the records is not claimed. This exact match does not evidence earlier coverage of the frozen claim or include the full comparison of both enumerators and extrema. The classical line-graph packing reduction and scalar maxima in its applicable regimes are credited, not counted as original.

## value

PASS

Rook graphs are natural complete-factor Cartesian products. Counting all and especially inclusion-maximal packings distinguishes the size spectrum of locally unextendable configurations from the known-style maximum packing problem. The exact minimum and complete two-exception classification quantify when maximality forces optimality, while wide boards exhibit a full parity-restricted support, information not supplied by a maximum alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
