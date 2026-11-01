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

Run `python3 verify.py` with Python 3.9 or newer from the directory containing the files. No third-party dependencies, external data, or network access are required.

The executable checks the complete set of directed multipaths for each of the parameters \(2\le n\le9\). It uses a ternary per-undirected-edge enumeration. For \(n\le7\) it independently constructs faces by testing every subset of arrows with indegree/outdegree constraints and explicit directed-cycle detection; the two lists agree exactly. It verifies the two embedded oriented top-sphere fundamental cycles by signed integer boundary cancellation, counts all top-dimensional facets, and reduces full simplicial boundary matrices over \(\mathbb F_2\) in exact arithmetic. The resulting reduced Betti groups agree with those predicted by the published homology theorem. For the three small polygons, it additionally checks the complete mixed-face descriptions; the five-vertex polygon has ten bridges and ten mixed triangles, whose relation graph is a connected ten-cycle.

Executed checks on the packaged source before acceptance ended with:

```
CHECK_OK n=2 base_vertices=3 faces_including_empty=13 betti_mod2={0: 1, 1: 2} case=two disconnected boundary triangles
CHECK_OK n=3 base_vertices=4 faces_including_empty=33 betti_mod2={1: 3, 2: 2} case=two boundary tetrahedra linked by four edges
CHECK_OK n=4 base_vertices=5 faces_including_empty=81 betti_mod2={2: 1, 3: 2} case=ten bridge edges identified by ten triangles in one cycle
CHECK_OK n=5 base_vertices=6 faces_including_empty=197 betti_mod2={2: 1, 4: 2}
CHECK_OK n=6 base_vertices=7 faces_including_empty=477 betti_mod2={2: 1, 5: 2}
CHECK_OK n=7 base_vertices=8 faces_including_empty=1153 betti_mod2={3: 3, 6: 2}
CHECK_OK n=8 base_vertices=9 faces_including_empty=2785 betti_mod2={4: 1, 7: 2}
CHECK_OK n=9 base_vertices=10 faces_including_empty=6725 betti_mod2={4: 1, 8: 2}
ALL_VERIFY_OK top_sphere_cycles small_n_geometry and_mod2_chain_ranks
```

These exhaustive **finite** computations neither prove connectivity for all parameters nor determine integral torsion. The all-parameter proof is the chain-level top-sphere analysis, the cited integral homology and connectivity results, the Hurewicz/Whitehead theorem application, and the elementary small-polygon geometry in `RESULT.md`. Independent mathematical validation has not been performed.
