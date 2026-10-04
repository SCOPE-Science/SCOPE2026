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

Run `python3 verify.py` with a standard Python 3 interpreter. The program contains the published 38-tetrahedron facet list, reconstructs every face, enumerates all 4095 nonempty induced vertex subcomplexes, and computes simplicial homology over \(\mathbb F_2\) by exact binary Gaussian elimination.

For every induced subcomplex it independently checks that the Euler characteristic from face counts equals the alternating sum of computed Betti numbers. It then builds the acyclicity-preserving vertex-deletion graph from the full twelve-vertex state, recomputes all layer sizes, identifies terminal states, counts maximal directed paths by dynamic programming, and checks that the three seven-vertex terminals are exactly the complements of the published exceptional deletion sets.

The expected success line is:

`VERIFY_OK acyclic_all=585 reachable=134 layers=12:1,11:11,10:36,9:52,8:31,7:3 terminals=8:17,7:3 maximal_paths=532 path_split=8:292,7:240 paper_terminal7=match`

Limits: this verifies only the stated \(\mathbb F_2\)-acyclicity and induced vertex-deletion claim for the published labeled complex. It does not test integral acyclicity, arbitrary face deletions, or a general family of balls.
