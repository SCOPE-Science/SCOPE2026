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

Run `python3 verify.py` with a standard Python 3 interpreter. The program has no third-party dependencies and no randomized choices. It constructs all 256 words, builds compatibility from the stated asymmetric distance, checks the radius-two descendant-ball equivalence for every pair, and performs a complete branch-and-bound clique enumeration. It then closes every maximum code under adjacent coordinate transpositions and, separately, global complementation.

The replay used for this package returned maximum size 7, 181440 labeled maximum codes, five coordinate-permutation orbits, and three coordinate-plus-complement orbits with sizes 20160, 80640, and 80640. The complete sorted census digest was `154a2b608261b4e4686ea9e83954a42852b7d82b6db2d27c7e5db7972b40bcff`.

The exhaustive computation proves only the finite length-eight statement. No extrapolation to other lengths or error radii is made. The symmetry computation classifies under the explicitly generated order-80640 group; it does not certify that this group is the full abstract metric-isometry group.
