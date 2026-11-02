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

# Verification record

Two standalone Python 3 programs use only the Python standard library. Execute `python3 verify_tournament_interchange_dynamic.py` and `python3 verify_tournament_interchange_orbits.py` from the directory containing these files.

The first checks completeness of a score-pruned enumeration of \(2640\) labelled regular tournaments on seven vertices, the full \(18480\) interchange-edge graph, \(14\)-regularity, bipartiteness, all-source connectivity and exactly three distance-sphere profiles. It enumerates all \(30\) labelled Fano triple systems by exact cover, checks the \(2,2,0\) cyclic decomposition counts on the three isomorphism classes, and identifies all \(360\) unordered diameter pairs as converse pairs.

The second constructs each labelled regular tournament from the three public seven-vertex catalogue representations under all \(5040\) label permutations. It applies an outgoing-neighbor-bitset encoding, independently reproduces all graph profiles from orbit representatives, computes the exact cyclic Fano systems, and checks the converse distances of \(7,7,9\). The class sizes \(240,1680,720\) exhaust \(2640\).

Finite exhaustive computation proves the particular seven-vertex metrics because the programs give a complete representation of their input domain and explicitly examine every legal neighbor. Running either program does not certify behaviour for arbitrary vertex counts or demonstrate independent scholarly validation. An inaccessible 1984 chapter creates a genuine unresolved historical-priority risk.
