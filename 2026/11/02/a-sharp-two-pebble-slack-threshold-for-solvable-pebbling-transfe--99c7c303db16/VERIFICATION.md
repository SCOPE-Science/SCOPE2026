---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The 14 Fano-incidence vertices are generated as point-line incidence with lines {i,i+1,i+3} mod 7. For a distribution D, the exact all-target reachable bitmask is support(D) union over all legal directed pebbling moves R(D-2e_u+e_v); each move decreases the pebble total so dynamic programming terminates. Every weak composition is enumerated for t=5,6,7,8: candidate counts 8568,27132,77520,203490, with solvable 0,161,5936,71323 respectively. Every legal unit jump and graph-edge slide is enumerated from each solvable distribution and counted once. A separately written, independently compiled C++ checker on this graph rederived jump-edge counts 0,42,33726,1145396 and slide-edge counts 0,42,11970,314496, with exact t=6 singleton/triple component signatures, t=7 jump components 2576 and 3360, slide components 21x24,28x74,3360x1, and t=8 connected for both. The t=7 capacity<=2 component split was checked by the source primary program and the independent enumeration; no solvable totals<5 by pebbling monotonicity. This is a FINITE exhaustive proof for t<=8, no claim about >=9.

## originality

PASS

The classical optimal-pebbling number and restricted optimal-pebbling notions are prior art; novelty is the complete labelled configuration-space exchange-graph classification and first connectivity at two slack pebbles on this natural Heawood graph. Source comparisons study scalar minimum and complexity, not adjacency/component graphs of all solvable distributions.

## value

PASS

The Heawood graph is a canonical 14-vertex cubic incidence graph. Full solvable-configuration reconfiguration graphs are natural nontrivial finite objects; the sharp 6-to-8 connectivity transition, 7-pebble capacity obstruction, and precise jump-versus-slide distinction are independently useful exact facts. An unfinished census at higher totals does not diminish the complete first-feasible-level classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
