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

The bundled `verify.py` is dependency-free and reconstructs the claim from definitions. It enumerates all 120 permutations, computes every Kendall-tau distance, constructs the compatibility graph for distance at least \(6\), enumerates all maximal cliques, independently enumerates all 5-cliques, and verifies that no maximum extends further.

It then checks that every maximum has ten internal distances equal to \(6\), constructs and pairwise-validates the stated 240 isometries, computes the two maximum-code orbits and stabilizers, identifies all maxima containing the identity, tests subgroup closure and inverses, enumerates their left cosets, and places the published Appendix-D witness in its orbit.

Recorded replay:

`VERIFY_OK vertices=120 edges=2940 bk_nodes=11350 maximal_hist=2:300,3:3120,4:3960,5:168 maximum=5 labeled_maxima=168 equidistant_maxima=168 group_size=240 orbits=2 orbit_sizes=48,120 stabilizers=5,2 normalized_maxima=7 subgroup_maxima=2 cosets_per_subgroup=24 published_orbit=120 generators=(1 2 4 3 5)|(1 2 5 3 4)`

The computation is exhaustive only for this finite parameter. It does not establish results for other lengths or distances and does not assert completeness of the chosen isometry subgroup among all metric isometries.
