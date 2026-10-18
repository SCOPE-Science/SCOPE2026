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

# Verification and scope

The complete finite certificate is the standalone `verify.py` in this package. Execute with `python3 verify.py` in the same directory. It uses only Python 3 standard-library integer arithmetic in \(\mathbb Z[\varphi]\), with the exact identity \(\varphi^2=\varphi+1\). The two independent determinant formulas are a three-by-three edge determinant and a four-by-four homogeneous determinant via all 24 permutations. All 27,405 vertex subsets are tested, with exact (irrationality-aware) signs, no floating-point approximations.

The program asserts the full 27-value histogram, the maximum signed magnitude \(28+44\varphi\) for doubled vertices, 60 maximizing vertex subsets, pair-codegree at most three, and 20 unique triangular facets each with three compatible maximizing completions. The geometric argument in `RESULT.md` is additionally needed to extend the finite enumeration to arbitrary contained tetrahedra and to exclude two simultaneously nonvertex corners. The containing volume is obtained separately by deleting 12 congruent vertex pyramids from the original icosahedron. The proof is not an automated certification of results for other polytopes.

Actual run: `VERIFY_OK original_icosahedron=12_vertices_30_edges_20_faces midpoint_polyhedron=30_vertices quadruples=27405 volume_levels=27 max_det=(28,44) max_sets=60 facial_families=20 max_pair_codegree=3`.
