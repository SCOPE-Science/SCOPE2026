---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Every tournament on seven labelled vertices corresponds to one 21-bit orientation; sound score-bound pruning enumerates precisely 2640 regular states. Exactly 14 cyclic triples in each (35 total minus 7*binom(3,2) transitive triples), so the interchange graph is 14-regular with 18480 edges; 3-bit flips imply bipartiteness. Independent complete all-source BFS found 3 profiles: sizes 240:(1,14,91,343,749,871,476,92,3), 1680:(1,14,91,340,739,853,483,113,6), 720:(1,14,91,336,721,822,485,147,22,1); graph connected, radius 8, diameter 9. Independent exact-cover recursion enumerated all 30 labelled Steiner triple systems, giving 2 cyclic Fano decompositions for 1920 states, 0 for 720. A seven-step converse path must reverse all 21 arcs once, hence is equivalent to a directed Fano decomposition; opposite parity excludes eight where none, and all-source BFS shows 720 exceptional states with unique antipode converse at nine, i.e. 360 unordered diameter pairs. Entire finite state space was enumerated, not a sample.

## originality

PASS

Established Brualdi–Li interchange-graph framework, connectivity, regularity and proposed seven-player diameter nine are prior. New assessed contribution is the full three-orbit distance-sphere census and exact cyclic-Fano converse obstruction and 360 antipodes; no inspected source gives these explicit results. Original 1984 chapter could not be accessed in full despite OA and authorized retrieval attempt: substantial qualified historical priority risk.

## value

PASS

The seven-player case is a canonical fixed-score tournament interchange network with a natural short-geodesic criterion. The complete reconfiguration metric and Fano-plane obstruction explain a meaningful structural transition (two directed decompositions or none) and provide an exact benchmark for sampling and interchange diameter work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
