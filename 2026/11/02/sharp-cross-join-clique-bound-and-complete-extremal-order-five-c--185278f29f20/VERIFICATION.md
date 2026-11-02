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

# Reproduction and scientific boundaries

Run `python3 verify_cliques.py` in the same directory as this file. It uses the Python 3 standard library and no external data. Successful completion prints `VERIFY_OK`, the full order-five maximal-clique size histogram, and a fourteen-vertex hexadecimal witness.

The program independently checks full-cycle truth tables and Euler-tour outgoing-order enumerations, matches their sets of 2048 order-five binary de Bruijn cycles, computes the fourteen-vertex cliques from complete star certificates, builds a graph from directly computed cyclic length-six factor intersections, and runs a generic Bron–Kerbosch enumerator. Both graph constructions agree on exactly sixteen fourteen-vertex cliques. The finite truth-table tests comprise all \(65536\) possible order-five binary feedback tables, not a sample. The proof of the all-order upper bound is combinatorial and does not rely on finite extrapolation.

Limitations: the sharp clique number beyond order five is not computed or proved. The literature comparison is based on material actually available; it does not establish independent publication-priority certification. The empirical computations were checked in a self-review only, not an independent audit.
