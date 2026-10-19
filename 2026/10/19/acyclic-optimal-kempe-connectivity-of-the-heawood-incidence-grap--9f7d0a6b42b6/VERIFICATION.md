---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Two compilable C++17 source files are included: `verify_a.cpp` and `verify_b.cpp`. Build with `g++ -std=c++17 -O2` and execute separately. `check_a.log` and `check_b.log` are actual program outputs.

Checker A constructs the cyclic Fano-plane incidence graph and applies recursive exact branch-and-bound edge-coloring, pruning exactly the creation of a bichromatic cycle, then enumerates normalized alternating-path switches. Checker B constructs the same abstract graph from the seven nonzero binary triples using incidence under the zero dot product, enumerates all proper edge-colorings before applying independent DSU acyclicity filtering, then constructs every normalized swap by BFS over an edge-component graph. Both check graph traversal and symmetry of adjacency.

Each checker found 119784 acyclic normalized states, 2874816 labelled states, 832440 undirected legal transitions, one component of size 119784, and the identical degree histogram. Checker B separately found 230336 proper normalized states. Source A prints elapsed seconds; this timing field is not deterministic and is not part of the mathematical certificate. All other integer results should reproduce across compatible C++17 runs.

The proof is an exhaustive finite case analysis, not an asymptotic assertion. The published general proper Kempe-equivalence theorem does not supply the acyclicity-preserving conclusion. Full independent external review has not been performed, and searches do not prove absolute publication novelty.
