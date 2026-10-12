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

The finite portion is replayable with `python verify.py`. The script constructs the nine points of \(\mathbb F_3^2\), the twelve affine lines, and the twelve complementary six-point blocks. It checks that every point belongs to eight blocks and that block-pair intersections have sizes \(3\) and \(4\), with the size-\(3\) graph equal to four disjoint triangles.

It then exhausts every permutation of the nine points and retains exactly those preserving the twelve blocks. The resulting set has size \(432\). Independently, it generates every affine map with invertible linear part and obtains the same \(432\) permutations. This proves the finite automorphism-group identification rather than sampling it.

The projective order \(18\) is a literature premise, not a computational output: Corollary 4.2 of arXiv:2008.09627 gives the complete automorphism group \(G_{18}\) of the associated Hesse-type index-two Halphen surface, and its proof shows descent to \(\mathbb P^2\). The source also states that surface automorphisms preserve the pencil. The proof in `RESULT.md` explains why stabilizing the twelve conics is equivalent, after blowing up the nine multiplicity-eight points, to lying in this surface automorphism group.

No claim is made about degenerate specializations or about automorphisms of the complement that do not arise from projective transformations preserving the conic set.
