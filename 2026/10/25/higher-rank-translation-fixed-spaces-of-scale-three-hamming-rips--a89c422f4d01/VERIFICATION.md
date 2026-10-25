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
# Mathematical and computational verification

The proof establishes an exact orbit-complex equivalence and exhaustive binary subgroup support patterns; finite enumeration is not an infinite proof.

`verify.py` constructs **each** rank-two, rank-three and rank-four linear subgroup of \(\mathbf F_2^n\) for \(2\leq n\leq6\), without using the proposed canonical generators to construct its observed orbit graph. Each affine orbit of each admissible subgroup is tested as a Rips simplex; edges are computed from all cross-orbit pairs. The graph is compared against the declared model by isomorphism, and triangle-freeness is tested. The run reported 3098 subgroups examined and 420 admissible cases, with the marker `HYPERCUBE_SCALE3_HIGHER_RANK_FIXED_VERIFIED`.

The checker requires only Python 3 standard library. Run `python verify.py` in the directory containing the package files. The finite enumeration covers the first examples and all four rank-two weight types; the unlimited theorem depends on the separate rank and support classification proof in `RESULT.md`.

This package has received a self-review only. The independent mathematical audit is not performed.
