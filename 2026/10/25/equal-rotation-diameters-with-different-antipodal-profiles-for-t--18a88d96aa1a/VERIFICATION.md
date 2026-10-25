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

# Computational verification

Execute `python3 verify_tubings.py` under Python 3.10 or later (standard library only). The script recreates the cube and Wagner adjacency relations, recursively enumerates 16,752 and 17,568 elimination trees as maximal tubings, and constructs every ridge flip. It compares each tubing's seven ridge neighbors with seven independently generated parent-child rotations, checks all 8! base-vertex permutations for automorphisms, and performs BFS from every automorphism-orbit representative. It checks the complete twenty-bin shortest-distance distributions, eccentricity profiles, radius 17, and diameter 20 for each graph, and prints `VERIFY_OK` on success.

An additional standalone C++ all-source breadth-first computation, separate from the orbit-weighted computation, was run on the generated adjacency graphs and agreed in all twenty positive distance bins. The Python script remains the complete reproducible verifier for the stated claim.

This establishes an exact finite census for two specified base graphs. It does not establish general formulas for elimination-tree rotation metrics of other graphs or independently verify originality against every unpublished calculation.
