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

# Reproducibility record

The exact claim is about all 16-vertex connected-dominating configurations of each of two fully specified graphs, for cardinalities four, five and six. The source files `verify.py` and `verify_alt.cpp` are complete and standalone, and construct adjacency from coordinates without external data. They independently enumerate all nonempty bitmasks (65,535 candidates per graph) and test every subset with up to six selected vertices for domination and connectivity. The checkers construct every one-element exchange, verify the edge and component counts, and perform breadth-first search from every five-vertex configuration to establish eccentricity distributions. A connected-component breadth-first search at six establishes the rook threshold. Four-vertex equality cases have additional explicit structural checks in Python.

Execute `python3 verify.py`. A successful execution ends `ALL_VERIFY_OK`. For the independent implementation, compile with `c++ -std=c++17 -O2 -Wall -Wextra -o verify_alt verify_alt.cpp` and run `./verify_alt`; successful execution ends `INDEPENDENT_VERIFY_OK`. Each checker uses the full finite universe and terminates deterministically. Neither a timeout nor a sampled subrange is interpreted as a proof.

Checked output: Shrikhande state/edge/component triples are (32,0,32), (672,5136,1), (4064,74304,1); rook triples are (8,0,8), (384,2112,2), (3744,63024,1). Five-state eccentricities: Shrikhande 672 of eccentricity five; rook 96 of eccentricity six and 288 of eccentricity seven. All claimed computations were executed successfully from the presented sources. These computations provide a finite proof of their exact combinatorial statements and are not an external independent research audit.

Limits: no infinite graph family is asserted. The proof depends on complete, inspectable finite enumeration for the larger exchange graphs, supplemented by conceptual minimum-set and rook orientation arguments. Independent scholarly auditing has not been performed.
