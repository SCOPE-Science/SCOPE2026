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

The package contains `verify.py`, a dependency-free Python verifier. It regenerates the admissible word set, compatibility graph, every maximal clique, an independent list of all six-cliques, the universal distance matching, and the orbit decomposition under the explicitly stated 64-element subgroup.

A fresh packaged replay produced `verification_output.txt`, whose first line is:

`VERIFY_OK eligible_vertices=72 edges=1168 maximal_cliques=2240 maximal_hist=2:64,4:640,5:1024,6:512 maximum=6 labeled_maxima=512 self_rc_distance=4 distance4_matching=3 all_other_pairs_distance=3 group_size=64 orbits=14 orbit_sizes=32x12,64x2 stabilizers=2x12,1x2`

The exhaustive computation is finite. It proves no statement outside the exact parameter \(n=4\), GC-content \(2\), and threshold \(d=3\), and the symmetry calculation concerns only the subgroup defined in the result.
