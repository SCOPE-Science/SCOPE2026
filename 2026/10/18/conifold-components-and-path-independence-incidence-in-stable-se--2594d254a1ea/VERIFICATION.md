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

Run `python verify_path_stable.py` with Python 3.9 or later. The program has no nonstandard dependencies. It enumerates all stable-set vertices of paths with \(3\le n\le7\), generates every nonempty face from the complete facet list, and computes active-normal ranks over the exact rational field. It checks facewise nonsimpliciality against precisely the predicted \(0,1,0\) faces, confirms inclusion-maximal singular faces, and checks all intersections of candidate singular components against nonconsecutive-center subsets. It also checks primitive normal vectors and all three-by-three determinants of the transverse conifold cone. The observed final line is `VERIFY_OK`.

The universal proof depends instead on the totally unimodular augmented-path incidence matrix, its graphic circuits, and the four-generator conifold semigroup explicitly established in `RESULT.md`. Finite enumeration does not establish the theorem for untested lengths. The code does not compute scheme-theoretic singularities at multiple-component intersections, and independent audit has not been performed.
