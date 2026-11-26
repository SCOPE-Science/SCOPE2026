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

Independently generated all cyclic tours of the 32 five-bit states by distinct-state DFS from state 00000, with closure checked after the 32nd state. Every rotation class includes 00000 once; each resulting feedback mask records the two possible successor matchings at each common four-bit suffix, so it is a unique label. To form adjacency, a successor swap at the first chord cuts the tour into its two arcs. The second swap rejoins exactly when its two visits lie on opposite arcs, which is precisely chord alternation. The independent replay built adjacency from that criterion, not the frozen BFS, subset DP or expected histogram. Successive exact int64 adjacency powers A^k give walks of length k; the first positive power for each distinct pair gives its distance and that entry counts geodesics. No overflow is possible since the maximum row degree to the seventh power is below 2^63. Replay found 2,048 vertices, 38,704 edges, all-pair distance histogram (38704,305376,758800,710976,254800,27104,368), maximum seven, and verified the half-Hamming formula. At distance seven, A^7 agreed row-for-row with all 368 frozen CSV counts; it reproduced all 14 values and frequencies and the stated extremes. The frozen BFS and complementary-coordinate DP were inspected, not executed. Their recurrence is also sound: the terminal XOR requires 14 sign changes in 7 two-flip steps, so every changing coordinate is flipped once and every path is counted by legal subset chains. Minor documentation caveat: the frozen checker uses int.bit_count(), so the stated Python 3.9 minimum should be read as 3.10; this does not affect the exhaustive independent result.

## originality

PASS

Existing same-order work covers the graph, valencies and metric/end-point information. None of the inspected strongest same-domain claims gives or mechanically implies the complete per-diametral-pair multiplicity spectrum without a different graph-path computation. The confirmed distinctive result is the fourteen frequencies of shortest paths to fixed farthest endpoints, not the degree distribution, distance-seven shell count or distance formula.

## value

PASS

The diametral pairs are the full intrinsic extremal domain of the standard reconfiguration graph, not an arbitrary subset. Their geodesic counts measure how many equally economical changes exist, and the fourteen values distinguish even pairs with the same maximum metric distance. The natural complete exact dataset provides a usable finite benchmark and answers a structural question not supplied by the known shell or valency data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
