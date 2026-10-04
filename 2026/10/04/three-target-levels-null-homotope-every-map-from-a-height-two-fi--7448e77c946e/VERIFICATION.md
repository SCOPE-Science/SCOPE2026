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

The proof is symbolic and quantified over all finite source posets with no three-point chain and all ordinal sums of at least three nonempty antichains. Its critical checks are:

1. The source decomposes as a lower side and an upper side because a point with both a strict predecessor and strict successor would create a three-point chain.
2. Lowering lower-side images from the top two target levels to level \(h-2\) preserves monotonicity and yields \(f_1\le f\).
3. After that operation, lowering top-level upper-side images to level \(h-1\) preserves monotonicity and yields \(f_2\le f_1\).
4. The image of \(f_2\) avoids the top target level, so \(f_2\) is pointwise below a top-level constant.
5. Pointwise comparable maps between finite Alexandroff spaces are homotopic.
6. Two target levels are insufficient: the identity of the four-point crown acts nontrivially on first homology, unlike a constant map.

The standalone verifier exhaustively checks the explicit construction on all bipartite source relation patterns with each side of size at most two and on four target weak-order profiles with three or four levels. It checks every monotone map in those cases. Expected output:

`VERIFY_OK source_cases=104 maps=18598 sharp_height2=checked`

The finite exhaustive check is a stress test only; it does not replace the general proof. Independent audit has not been performed.
