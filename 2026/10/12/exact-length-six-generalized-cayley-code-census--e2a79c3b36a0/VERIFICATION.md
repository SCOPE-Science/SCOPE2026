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

Run `python3 verify.py`. The script uses only the Python standard library. It independently constructs every generalized transposition on six positions, performs breadth-first search of the resulting Cayley graph, constructs the full minimum-distance-three compatibility graph, enumerates every maximal clique, checks the full list of maximum codes, tests the identity-containing maxima for subgroup closure, and computes the left-multiplication orbit partition.

Expected terminal line:

`VERIFY_OK generators=70 distance_hist=0:1,1:70,2:469,3:180 vertices=720 edges=64800 degree=180 maximal_cliques=758976 maximal_hist=4:670320,5:82656,6:6000 maximum=6 labeled_maxima=6000 normalized_maxima=50 subgroup_maxima=2 left_orbits=10 orbit_sizes=120x2,720x8 subgroup_generators=(1,2,4,6,5,3);(1,3,2,6,4,5) bk_nodes=1458354`

The exhaustive domain is exactly all \(720\) elements of \(S_6\). The verifier does not extrapolate beyond this finite parameter. It proves completeness by enumerating every maximal clique in the compatibility graph, not by stopping after a witness is found. The left-orbit computation covers all \(6{,}000\) maxima but does not assert that left multiplication is the full metric-isometry group.
