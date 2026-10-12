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

The bundled `verify.py` uses only the Python standard library. It checks the Levenshtein distance independently by dynamic programming and recursion on all unordered word pairs, enumerates all four-word and five-word candidates, proves the maximum size and exact count, verifies every maximum is an affine \(2\)-flat, and enumerates the full compatibility-graph automorphism group by adjacency-preserving backtracking. It then computes all maximum-code orbits and the two pair-distance profiles.

Observed replay:

`VERIFY_OK vertices=32 edges=211 maximum=4 labeled_maxima=28 affine_maxima=28 directions=14 admissible_cosets_per_direction=2 automorphism_group=4 max_orbits=8 max_orbit_sizes=2,2,4x6 direction_orbits=8 direction_orbit_sizes=1,1,2x6 distance_profiles=18x(3^5,4),10x(3^4,4^2)`

No claim is made beyond binary length \(5\), minimum edit distance \(3\). The originality conclusion depends on the inspected literature and database searches and retains the stated risk of obscure unindexed finite enumerations.
