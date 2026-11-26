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

A matching is maximal iff its uncovered set is independent. Independently enumerated all independent uncovered sets of size 20−2k in GP(10,3), then all perfect matchings of their induced complements, for every 0≤k≤10. Pairing the least remaining vertex with each available neighbour finds each such perfect matching once, and distinct uncovered sets cannot duplicate a state. The check used pairwise XOR of edge masks with popcount two for adjacency and bitset breadth-first frontiers from every state for component sizes and diameters. Run: python3 /workspace/independent_checks/desargues_exchange.py. It returned only layers 6–10, with state counts (5,120,1620,1120,60), edge counts (0,120,3360,2160,0), component sizes 5×1, 30×4, 1×1620, 1×1120, 60×1 and corresponding diameters (0,2,14,12,0). Size-seven states all have degree two, establishing the 30 cycles. The state sum is 2925. At size ten a one-edge replacement would have to join the very same two endpoints, impossible with a different edge in this simple graph. Both recorded outputs agree, but the independent enumeration, not the recorded outputs, is the fresh finite check.

## originality

PASS

The substantive claim is the maximal-only exchange structure across sizes, particularly the 30 four-cycles and the exact connectivity and diameters of both middle layers. Prior same-graph matching counts and local-pooling evidence, and general matching reconfiguration results, do not supply those facts. The known minimum size, known perfect-matching count and elementary perfect-layer isolation are not credited as original individually.

## value

PASS

On a canonical cubic bipartite graph already used to study maximal matchings, the size-preserving move gives distinct behaviours: rigid saturated minima, small cyclic components, two connected intermediate layers with exact path-length bounds, and rigid perfect states. This supplies an exact benchmark for reconfiguration with maximality imposed, where ordinary matching-complex data or unconstrained reconfiguration are not enough. It is a useful finite invariant, not a generalized Petersen family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
