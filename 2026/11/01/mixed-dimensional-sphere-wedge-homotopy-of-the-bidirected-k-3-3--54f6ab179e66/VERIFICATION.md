---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For D=bidirected K_{3,3} (18 arcs, six vertices), multipaths are exactly arc sets with indegree/outdegree <=1 and no directed cycles, including nine forbidden two-cycles. Independently enumerated all 2^18-1 masks: 714 nonempty faces, f=(18,108,264,252,72). Reconstructed the specified coordinate matching with 341 legal pairs, entire 2376-incidence oriented Hasse digraph acyclic, critical cells one 0-cell, 19 dimension-3 and 12 dimension-4. Independent exact signed integral gradient-path recursion yields the zero 19x12 degree-four Morse boundary; original result/verifier prove the same. Hurewicz pi_3(wedge^19 S^3)=Z^19 shows every 4-cell attachment null, giving wedge^19 S^3 vee wedge^12 S^4. Mod-2 ranks alone would not prove this integral homotopy.

## originality

PASS

The assertion is about the bidirected complete bipartite multipath complex, not the bidirected polygon, unidirectional chessboard complex or undirected Morse/matching complex. Independent Resultary queries did not find the asserted 19/12 homotopy type. It does not follow by specialization of the inspected published general results; priority remains best-of-knowledge only.

## value

PASS

The bidirected K3,3 is the smallest balanced cubic complete bipartite graph, with directed 2-cycles obstructing the usual acyclic blow-up theorem; the exact 19/12 wedge establishes a natural mixed-dimensional integral homotopy benchmark. It is not just an Euler-characteristic or field-Betti recomputation, and no family-wide extrapolation is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
