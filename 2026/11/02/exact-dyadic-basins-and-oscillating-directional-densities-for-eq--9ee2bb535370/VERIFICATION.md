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

# Verification notes

The key symbolic steps independently checked in the proof are the orthogonal projection parameters, the farthest-distance comparison, the outer affine radius recurrence, the inner contraction, and the even/odd dyadic shell lengths. On complete supporting lines, the two parameter descriptions of any triangle vertex yield exactly the same next point.

Run `python3 verify.py` with Python 3 and no third-party packages. It checks literal Euclidean projections by exact rational arithmetic in a Gram-matrix basis, tests 6147 rational initial locations and 135 iterates per location, verifies 16 levels of midpoint-preimage exceptions and 19 shell endpoint identities, and prints `CHECK_OK 6147 exact geometric projection and basin tests; exact dyadic endpoints and two cycle equations`. These finite checks cannot establish a universal real-parameter result. The universal claim rests on the explicit recurrence and elementary summation.

The first publicly verified source date is January 7, 2021, taken from the publisher metadata; the journal issue date and later author manuscript upload are different. Primitive three-cycle existence is previously classified and is not advanced as original here. No external independent audit has been carried out.
