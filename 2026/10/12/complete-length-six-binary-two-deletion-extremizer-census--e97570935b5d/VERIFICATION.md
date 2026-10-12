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

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses only the standard library and reconstructs every binary word of length \(6\), every exact two-deletion descendant set, and the full compatibility graph.

The script checks descendant generation both by direct survivor-position choices and by two iterated single deletions. It verifies \(64\) vertices and \(522\) compatibility edges, exhaustively enumerates all maximal cliques, and separately enumerates every four-clique. The two equality-case enumerations agree exactly. It then recomputes the universal core, the Hamming weights of the nonconstant members, every 2-dominance relation, and the complete reversal/complement action on the optima.

Expected successful output:

`VERIFY_OK vertices=64 edges=522 bk_nodes=620 maximal_hist=2:217,3:276,4:16 maximum=4 labeled_maxima=16 core=000000,111111 middle_weight=3 group_size=4 orbits=7 orbit_sizes=1,1,2,2,2,4,4 basic_maxima=3 basic_orbits=2 basic_orbit_sizes=1,2 coverage=8:1,11:2,12:6,14:1,16:6`

The computation is exhaustive only for \(n=6,t=2\). Finite enumeration here is not evidence for any larger length, other deletion count, or a larger automorphism group. The supplied `census.csv` is derived data; `verify.py` is the primary reproducibility artifact and does not trust the CSV.
