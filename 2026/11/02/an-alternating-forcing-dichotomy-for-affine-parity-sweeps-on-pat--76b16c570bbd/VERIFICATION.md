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

The exact statement follows from the explicit isomorphism between path states and the zero-sum hyperplane of one additional coordinate, affine adjacent-coordinate swaps, and a fixed-point calculation on the cycles of a permutation. The proof covers all path sizes at least two, all finite fields of characteristic two, all offset vectors, and all permutation sweep schedules.

To reproduce finite checks, execute `python3 verify.py` alongside `verify_output.txt`. The checker carries out independent vertex-update and coordinate-swap calculations; 4,696 exact offset/schedule parameter cases comprise 154,528 initial-state checks. There are 936 further seeded local-conjugacy and power-identity tests, through path length 40. The exact printed success marker is `AFFINE_PATH_ORBITS_VERIFY_OK`.

Finite enumeration cannot certify the infinite family. The needed all-size steps are proved in `RESULT.md`: independence of path-root vectors, adjacent-transposition Coxeter cycle, the image of the cyclic difference map, the path-adjacency rank condition, and the gcd-dependent affine-hyperplane count. Full historical equivalence is not ruled out by the sources inspected. Independent audit has not been performed.
