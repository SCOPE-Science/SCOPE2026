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

# Reproducible verification

The two Python 3 programs under `scripts/` use only the standard library. Each reconstructs the 28-vertex Coxeter graph from a different exact combinatorial presentation and independently reconstructs the 84 seven-edge induced matchings. One uses Bron–Kerbosch maximal-clique enumeration; the other exhaustively searches fixed-size cliques to confirm the absence of an eight-edge induced matching. Both enumerate all 3,486 unordered optimum pairs and compute all distances in exact-one- and exact-four-replacement graphs.

`python3 scripts/verify_fano.py` confirms the distance-three sphere description, 28 one-replacement triangles, the unique lateral-edge correspondence over distance-three Coxeter pairs, and 56 triangles in the exact-four exchange graph.

`python3 scripts/verify_stars.py` independently verifies optimum cardinality and count, uniform distance shells and an explicit 56-vertex graph-isomorphism bijection against the published SageMath `Klein3RegularGraph` adjacency encoding. The data source is https://github.com/sagemath/sage/blob/develop/src/sage/graphs/generators/smallgraphs.py .

The resulting finite checks are exhaustive and deterministic, but they are not an infinite-parameter proof, a complete literature-priority guarantee, or an independent scholarly audit.
