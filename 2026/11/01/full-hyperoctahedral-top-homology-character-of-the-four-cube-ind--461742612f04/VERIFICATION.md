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

Run `python3 verify_q4_symmetry.py` in any Python 3 standard-library environment. This enumerates all 743 independent vertex subsets of the four-dimensional cube, reconstructs augmented simplicial boundaries, computes all mod-two ranks, then checks the signed homological Lefschetz trace in two separate ways for all 384 affine signed-coordinate automorphisms. Finally it checks all 20 signed permutation conjugacy classes, the translation Fourier multiplicities and the predicted sign-twisted standard representation on the translation-fixed sector.

The successful output is supplied verbatim in `verification_output.txt` and begins with `Q4_INDEPENDENCE_SYMMETRY_VERIFIED`. These finite checks certify the claimed specific rational character by exhaustive counting plus the homological-concentration argument. They are not an independent audit; no general-dimensional cube assertion, integral symmetry-lattice classification, or unindexed-publication-priority certification follows.
