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

An independently written exact replay (python3 /workspace/audit_chvatal.py) generates cycles as connected unions of two disjoint perfect matchings. Every Hamiltonian cycle in this even-order graph has exactly one unordered partition into its two alternating matchings, so the enumeration is complete and unduplicated. For each resulting cyclic order, deleting two disjoint edges cuts two paths; there is exactly one other matching of their four endpoints that rejoins them into a single cycle, and the replay tests both of those new edges against the input. Shared-endpoint deletions cannot give a nontrivial degree-preserving switch. Exhaustive BFS on the resulting adjacency gives 185 vertices, 382 edges, a single component, radius 6, diameter 9, degrees 2:21,3:48,4:60,5:28,6:6,7:18,9:4, eccentricities 6:12,7:104,8:53,9:16, and unordered distances 1–9 of 382,1129,2694,4116,4876,2992,713,110,8. A distance-nine witness has cyclic orders (0,1,7,8,2,3,9,11,6,10,5,4) and (0,9,10,8,4,3,7,11,5,1,2,6). These statements are about Hamiltonicity-preserving switches in the given graph; there is no separate notion of a TSP optimum in the hypotheses. The independent generation and reconnection tests differ from both supplied generation routines and their mask comparison.

## originality

PASS

The Chvátal graph, its tour count and the switch operation are known. The assessed distinct result is the exact connected switch graph's size, radius, diameter and distributions for this graph. The strongest inspected papers and catalogue overlaps give the general operation and different settings or the known state count, not the target adjacency and metric census.

## value

PASS

The standard sparse, triangle-free 4-chromatic graph is a natural named test outside the cited positive reachability regimes. The exact census gives an independent benchmark for Hamiltonian-constrained 2-opt: every tour is reachable while some pairs require nine exchanges, and the attainable eccentricities and counts distinguish central and worst cases. This is more than recomputing the known number of tours, but it makes no claim on mixing or other graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
