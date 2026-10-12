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

Run `python3 verify.py` in the package directory. The verifier uses only the Python standard library. It rebuilds the 12 allowed error patterns, checks compatibility both by direct ball intersection and by the difference set, verifies the projection-bound kernel containment, enumerates all four-cliques, proves none extends to five words, checks affine closure, counts the 12 direction planes and all 16 cosets per direction, and verifies the translation-plus-reversal orbit decomposition.

Expected output:

`VERIFY_OK vertices=64 errors=12 bad_differences=44 edges=640 maximum=4 labeled_maxima=192 affine_maxima=192 directions=12 cosets_per_direction=16 natural_group_size=128 orbits=7 orbit_sizes=16x2,32x5 direction_orbits=7 direction_orbit_sizes=1x2,2x5 profile_class_sizes=16,32,32,48,64`

Limits: this replay certifies only the finite length-six noncyclic model and the declared order-128 action. It does not determine the full automorphism group or make claims for other lengths or cyclic adjacency.
