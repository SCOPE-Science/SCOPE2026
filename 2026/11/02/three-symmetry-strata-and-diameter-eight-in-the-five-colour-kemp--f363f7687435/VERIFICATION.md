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

The original numerical assertions were correct. The repaired claim keeps the full labelled state graph and narrows the contribution to its Kempe-move invariants. A proper colouring is exactly a Latin rectangle, with each row a permutation and each column injective. Each legal move is enumerated by grouping the six bichromatic edges by endpoint connectivity and switching the edges of exactly one whole component. This move preserves properness and is an involution on that component. First-row normalization is unique; enumerating all row and column permutations then renormalizing removes precisely the colour action for the sole purpose of orbit classification. I checked the independent replay's enumeration, union–find component construction, orbit partition, reciprocity check and FIFO BFS. Its full calculation found 66,240 states, 1,094,400 directed incidences, 547,200 edges and the three stated orbit sizes and degrees. From the three representatives BFS reached all 66,240 vertices with profiles (1,15,180,1480,8302,27868,26713,1675,6), (1,16,182,1472,8243,27793,26899,1634), and (1,17,191,1540,8609,28689,25974,1219). Automorphism invariance establishes every vertex's eccentricity, so radius 7 and diameter 8 follow. The repairs additionally state exact consequences checked directly: 25,920 unordered diametral pairs (6 per each of 8,640 eccentricity-eight states, divided by two) and 57,600 central states. The alternate frozen program prints the profiles but does not assert their equality; the primary one and independent replay do assert the full profiles.

## originality

PASS

Originality fails for the unqualified original three-stratum classification as a new finding: McKay already tabulates the three exact isotopy classes of order 5×3, the identical group action in opposite dimension notation. The repaired finding instead treats the state and isotopy enumeration as background, uses the known classes to index the full exact Kempe distance profiles, and claims the resulting graph census and geometry rather than rediscovery of those classes. That distinct remainder survives comparison with the strongest available strict-Kempe and Latin-rectangle recolouring results.

## value

PASS

The repaired theorem answers the exact reconfiguration question in a natural small Latin-rectangle case at the chromatic index, where allowing defective intermediates changes the mathematical problem. It provides a benchmark stronger than reachability or a count: every state's eccentricity and full distance distribution, the peripheral and central classes, and the precise maximal detour. The value is the move geometry, not a recomputation of the known isotopy table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
