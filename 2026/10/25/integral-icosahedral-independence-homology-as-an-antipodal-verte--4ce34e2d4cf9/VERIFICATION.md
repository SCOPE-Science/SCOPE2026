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

# Reproducibility and scope
Run `python3 verify_icosahedron.py` in a directory with `networkx` installed as specified by `requirements.txt`.

The executable constructs exactly thirty edges of the chosen graph, enumerates 12 independent vertices, 36 pairs and 20 triples, proves no four-vertex independent simplex exists, and verifies that 30 of the 36 complementary edges each lie in two triangles while six lie in none. It checks the induced triangle subcomplex has the combinatorics of a triangulated two-sphere: 12 vertices, 30 edges, 20 triangles, all twelve vertex links cycles of length five, and Euler characteristic two. The script verifies the explicit isomorphism of this distance-two graph with the original icosahedral graph, and that its six omitted edges are exactly the distance-three antipodal pairs.

It then constructs an integral 2-cycle from signs on the twenty oriented triangles, checks all 120 graph automorphisms preserve the subcomplex, identifies the central antipode and the 60-element orientation-positive subgroup, and verifies all degree-one signed-permutation character traces by order. The exact expected class counts are: positive-degree elements \((1,15,20,24)\) by rotation orders \((1,2,3,5)\), and their 60 negative-degree antipodal products. The generated output ends in `VERIFY_OK_ICOSAHEDRAL_INDEPENDENCE_INTEGRAL_MODULE`.

The finite code confirms discrete combinatorial premises. The integral relative long exact sequence, homotopy equivalence, and character decomposition are mathematical arguments in `RESULT.md`, not claims inferred from modular ranks or test extrapolation. Independent scientific validation has not been performed.
