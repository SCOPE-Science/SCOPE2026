---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Mathematical checks

- The perimeter identity is derived from the published hole-free Euler relation and the count of the four sides of each square.
- The four-center obstruction is checked by the induced adjacency graph: at most two adjacent edges gives pair-intersection sum at most 8; three edges give a path or star and the same bound; four edges force one square face and a 13-tile incidence union.
- For three centers, zero or one adjacent pair cannot fit in 11 tiles. Two adjacent pairs form a path, and the five-cycle link has exactly two neighbor-pair orbits, yielding the two constructions.
- Each construction has 11 tiles, three interior vertices, no hole, and perimeter \(2\cdot11+2-2\cdot3=18\).

## Limits

The result is a hand proof based on local incidence and published extremality facts; no computer enumeration is claimed. The literature searches found no direct matching enumeration, but absence from search results is not a proof of novelty. Independent audit and independent validation remain unperformed.
