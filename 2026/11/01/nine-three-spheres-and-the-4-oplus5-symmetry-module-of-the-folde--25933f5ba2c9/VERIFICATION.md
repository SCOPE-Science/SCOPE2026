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

# Reproduction and limits

Run `python3 verify.py` using Python 3.10+ with no third-party packages. The script defines the sixteen even-parity five-bit graph vertices and distance-four adjacency without external graph tables. It checks regularity, all 120 nonadjacent common-neighbor counts, the pairwise zero common-neighbor condition, 393 independent subsets via two distinct generators, f-vector `(16,80,160,120,16)`, and the exact lexicographic discrete Morse pairing.

It directs every nonempty face-incidence upward exactly when matched and downward otherwise and checks a complete topological sort over all 392 vertices and 1200 Hasse arrows; this proves that finite matching acyclic. Its output includes `ordinary_pairs=191 critical=(one_vertex,nine_3_cells)`.

It enumerates 120 coordinate permutations and 16 translations, verifies 1920 distinct graph automorphisms, and calculates their rational degree-three homology traces as signed simplicial Lefschetz traces. For every automorphism, it separately enumerates independent unions of vertex orbits and compares the resulting independence polynomial at -1 against both the signed trace and the closed character formula. It also checks Fourier multiplicities on all 16 characters of the translation subgroup and traces of the averaged four-dimensional invariant projection. No numerical approximations or probabilistic tests are used.

Observed replay result: `RESULT_OK wedge_of_9_S3 and rational_H3=sign_tensor_standard4 plus sign_tensor_weight1_module5`. This supports the exact finite proof, including the representation identification. The rational decomposition does not certify an integral direct-sum decomposition, and the homotopy result is not asserted equivariantly. Independent external assessment has not been performed.
