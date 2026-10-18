---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Unique-response conditions require vertices labeled ≥2 to form a graph-theoretic 2-packing (distance at least 3): adjacency contradicts positive-label exclusion, distance two gives a vertex with two defenders or a positive vertex adjacent to one. In crown graph all same-side pairs have distance two, cross-side pairs are adjacent except a deleted matched pair, so the strong set is ∅, a singleton, or exactly one deleted pair. Empty forces all ones. Singleton defender d forces all its n−1 neighbors zero, every other nond vertex one, and defender label exactly h. A matched pair forces remaining vertices zero and each strength h. These disjoint cases yield counts 1,2n,n and the weight formula. Fresh independent exhaustive all-(h+1)^(2n) labelings for n=3,4,5 produced weight tables {4:3,5:6,6:1}, {6:4,7:8,8:1}, {6:5,8:10,10:1}; arbitrary n follows from structural classification.

## originality

PASS

Mojdeh et al. (2021) prove a general 2-packing minimum formulation and complete-bipartite values; neither enumerates all feasible crown functions. A 2026 ordinary strong Roman crown value has same minimum scalar but does not impose unique-response conditions or count all three families. Relevant Resultary crown finding treats perfect Roman domination (fixed defender weight 2), not the high-label strong Roman variant.

## value

PASS

Provides complete weight enumerator rather than only optimal value for a natural and highly symmetric family. Separates unique-response from ordinary strong Roman and quantifies rigidity of one-edge matching deletion from complete bipartite graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
