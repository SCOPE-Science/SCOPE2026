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

# Verification of the joint icosahedral law

Install `requirements.txt` and run `python verify.py`. The program uses exact symbolic arithmetic for the six antipodal normals, all 20 triple determinant tests, vertex/face chamber sign vectors, 30 edge-crossing counts, and 60 neighbor–Voronoi midpoint containment checks. It independently verifies that the 12 vertex rays give decagons and the 20 face-normal rays give dodecagons, exhausting 32 general-position arrangement chambers. Numerical polar integration then checks the elementary spherical-segment formula over different thresholds, and a fixed-seed 30,000-orientation experiment checks a sample of the joint law. The observed output is `ALL_EXACT_ARRANGEMENT_AND_AREA_CHECKS_PASSED`.

The full continuum statement relies on the proven spherical cap–polygon integration and geometry, not on numerical sampling. Numerical tolerance tests cannot certify an identity without that proof; the algebraic sign tests are exact. Independent mathematical audit has not been performed.
