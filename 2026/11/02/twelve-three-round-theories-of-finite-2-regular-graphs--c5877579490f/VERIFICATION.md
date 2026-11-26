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

After two moves, equality, adjacency and the set of third-point incidence patterns are the exact one-round invariant. At order at least seven a distinct vertex adjacent to neither named vertex always exists. For adjacent distinct vertices, the remaining neighbors coincide precisely on a triangle; for nonadjacent ones the common-neighbor counts 0, 1 and 2 have distinct pattern sets, with count 2 precisely at opposite vertices of a square. Hence the set of pair types extending a vertex identifies triangle, square or longer cycle; each admits a far partner by another component or by distance at least three. Taking sets once more gives exactly the three cycle-presence bits, with no counting of multiplicities. A dominating pair separates all five small cases from the large orders. Triangle existence, a nonadjacent pair, nonadjacent twins, and a nonadjacent pair with no common neighbor provide the stated small-case distinctions. The minimum orders for the seven large signatures are attained by cycle partitions as listed; the full signature costs at least 3+4+5 vertices and has only one partition at that minimum. The square witness uses a universal third quantifier, but is indeed rank three. A fresh exact recurrence on adjacency/equality patterns reproduced 12 fingerprints across 572 partitions through order 24.

## originality

PASS

Credit the established connected-cycle tail and overlapping restricted long-cycle union equivalences. The inspected statements do not give the complete rank-three partition for arbitrary unions, the mixed short-cycle interactions, or the optimum twelve-vertex bound. Pass is for that complete disconnected classification, not the connected cases or the standard EF recurrence. Historical priority is provisional.

## value

PASS

The result decides every comparison in a natural unbounded graph family. At rank three the small-order domination exception interacts with the cycle kinds, and a repeat of a cycle that is distinguishable from a long connected cycle can become indistinguishable from it. This is a precise benchmark for low-rank graph types and disjoint-union composition, with a tight representative bound rather than a census at an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
