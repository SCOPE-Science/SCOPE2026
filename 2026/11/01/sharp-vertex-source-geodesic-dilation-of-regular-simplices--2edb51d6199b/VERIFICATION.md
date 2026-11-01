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

The self-contained `verify_simplex_dilation.py` runs symbolic checks of the simplex-altitude, opposite-facet inradius, source-to-centroid distance, and sharp distortion identities. The test executed successfully with 22,000 seeded barycentric samples across dimensions 2 through 23. The exact proof in `RESULT.md` establishes the theorem for every integer dimension at least two and every boundary target.

Finite sampling neither establishes unrestricted geodesic optimality nor verifies novelty. In particular, the test checks the constructive two-facet upper bound; the sharp lower bound and uniqueness are geometric arguments in the proof. No independent audit has been performed.
