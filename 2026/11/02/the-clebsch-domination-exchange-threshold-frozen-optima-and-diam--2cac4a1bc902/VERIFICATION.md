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

The closed neighborhoods have size six and intersect pairwise in two vertices (two adjacent endpoints, or two common neighbors for nonadjacent vertices), so a triple covers at most 14 vertices. The displayed four-set covers all 16. The finite result was independently reconstructed with `python3 /workspace/branches/independent-checks/record3.py`: vertices are subsets of a five-set modulo complements; distance-one cube edges fold to the stated graph. A candidate is rejected exactly when it is contained in the complement of a closed neighborhood, and all valid pairs are linked by intersection size k−1. The two four-set orbits each have size 40 (empty and 4-cycle) with no edges. At five the replay yielded 1056 states and 10320 edges, with 960 of degree 19 and 96 of degree 25. Coordinate permutations of the five-set and all folded translations give the same 1920 automorphisms as the Cayley generators. A stabilizer of the zero vertex embeds in S5: the other ten vertices are uniquely identified by the pairs of zero's neighbors with which they are adjacent. Thus the enumerated orbits are full, not merely subgroup orbits. The orbit sizes 16,80,160,320,480 have respective sorted induced degrees [0,0,0,0,0], [1,1,1,1,4], [0,1,1,1,3], [0,0,0,1,1], [1,2,2,2,3], which identify the stated types because the graph is triangle-free. Layer expansion from one vertex of each full orbit exhausts J5; both degree-25 orbits have shell profile (1,25,130,250,570,80), and all three degree-19 orbits have profile (1,19,94,316,507,119). Hence every vertex has eccentricity five and the graph is connected. Frozen verifiers were inspected, not executed. A replay-documentation caveat: although the original advertises Python 3.8, its Python checker uses int.bit_count(), which requires Python 3.10 or newer. This does not affect the scientific result or independent replay.

## originality

PASS

Pass only for the exchange threshold, exact jump metrics, and state-orbit classification, not for the feasible-state counts or minimum cardinality. An earlier Resultary dominance-complex result already tabulates 80 and 1056, and gives enough explicit data to reconstruct feasible states. Its reported invariants do not compute the equal-rank exchange connectivity, distances, and induced-type orbits; obtaining those from its files still requires a separate exact exchange analysis.

## value

PASS

The fixed-size move limit is a natural stability question on this symmetric classical graph. A researcher already knowing how many feasible states there are still needs to know whether local exchanges connect them, how much slack is needed, and the maximum number of moves. The complete four-to-five threshold and exact self-centered diameter and profiles distinguish frozen optima from mobility; the orbit classification identifies which configurations have which profiles. This value does not rest on retabulating the earlier face counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
