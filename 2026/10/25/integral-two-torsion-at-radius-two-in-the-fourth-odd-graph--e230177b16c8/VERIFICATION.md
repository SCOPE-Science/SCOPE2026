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

# Reproducibility

Execute `python verify_odd4.py` from this package with `sympy` installed according to `requirements.txt`. `verification_output.txt` is the execution output obtained from the actual packaged script. The program constructs all 35 three-subsets, checks every pairwise graph distance by BFS, enumerates all 56 maximal five-vertex cliques and their 1,211 nonempty faces, and checks each of 280 simplicial collapse pairs as an actual currently free face.

The collapsed two-complex has 280 edges and 336 triangles. A lexicographic spanning tree fixes 246 non-tree-edge integral coordinates. Signed triangle boundaries form an explicitly generated 246-by-336 integer matrix. The column Hermite-normal-form basis has diagonal multiset \(\{1\text{ (245 times)},2\text{ (once)}\}\), hence lattice index two. The separate mod-two rank is 245. Thus the exact integral result is not inferred from field ranks or Euler characteristics alone.

The certificate has no hidden data inputs; its sole nonstandard computational dependency is SymPy. Reexecution is an algorithmic verification, not an independent external audit, and the theorem is limited to the specified 35-vertex graph and inclusive graph-distance radius two. It does not certify a homotopy type.
