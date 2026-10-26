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

# Reproducibility and finite proof scope

The attached `verify.cpp` is a complete C++17 program. Compile with `g++ -std=c++17 -O2 verify.cpp -o verify` (do not define `NDEBUG`) and execute `./verify`.

**Universe.** With the specified eleven-vertex graph, all \(4^{11}=4,194,304\) named assignments are tested for proper colouring. A separately constructed recursive list contains exactly \(12,480\) valid states. Each state has a unique base-four index, so this is an exhaustive finite census, not a sample.

**Recolouring edges.** Every vertex and alternative colour is attempted. The predicate rechecks all twenty graph edges and the computed undirected edge list is checked for symmetry. The result is \(45,240\) undirected edges, with global degree multiplicities \(480,2640,3840,4320,1200\) at degrees \(5,6,7,8,9\).

**Connectedness, distances and symmetry.** Exhaustive BFS finds two components with \(6,240\) states each. BFS from **every vertex of both components** yields diameter \(17\) each. Every palette permutation and pentagon rotation/reflection is tested on a chosen state; because each gives a recolouring graph automorphism, the observed component action at that state extends to the entire component. Two explicitly given four-colourings are confirmed to lie in opposite components.

**Observed terminal markers:** `EXHAUSTIVE_UNIVERSE_OK`, `RECOLOR_GRAPH_OK`, `COMPONENTS_OK`, twice `COMPONENT_DETAIL_OK`, `SYMMETRY_OK`, and `VERIFY_OK`.

**Limits.** The finite complete census does not prove any analogous family-wide claim. The 5-colour mixing corollary depends on the cited general degeneracy theorem rather than a direct enumeration of five-colour states. The science has been subjected to self-review only; independent audit is not performed.
