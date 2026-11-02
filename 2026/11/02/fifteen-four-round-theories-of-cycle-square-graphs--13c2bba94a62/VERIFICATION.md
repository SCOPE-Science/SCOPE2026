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

# Reproducibility and limits

Run `sh verify.sh` with a C++17 compiler and Python 3. The verifier compiles `cycle2_orbit.cpp` and `cycle2_direct.cpp` from source and deletes its temporary executables. It checks the fifteen-class partition, the pairwise agreement of independently formed rank-four type identifications, and the four-selected-vertex pattern calculation. The completed output from the packaged sources is in `verification_output.txt`.

The direct verifier enumerates every ordered four-tuple, with repetitions, from each graph through order thirty-two. It recursively interns the atomic equality/adjacency diagram and set of one-vertex extension types until reaching the empty tuple of rank four. The orbit verifier uses dihedral symmetry to reduce tuple enumeration and checks orders through seventy-two. A dihedral symmetry preserves all adjacency and equality facts, so replacing a tuple by its orbit representative cannot alter its first-order type. The critical range five through nineteen is covered by both exact methods.

To reconstruct the mathematical infinite tail, interpret every adjacency atom of a square graph in its unsquared cycle by a nonloop edge or a two-step path, using at most one additional existential quantifier. Brown and Hoshino (2007), Theorem 4.9, proves the required rank-five cycle equivalence at sizes at least nineteen. This external theorem is a logical premise; the finite programs do not prove it.

The computations do not enumerate all written separating sentences, do not treat unbounded order in isolation, and do not constitute independent mathematical audit. Published-literature comparisons are documented in `AUDIT.json` and `REVIEW.md`.
