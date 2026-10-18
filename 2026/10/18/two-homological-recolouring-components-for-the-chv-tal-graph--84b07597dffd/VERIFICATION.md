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

# Reproducible mathematical checks

Run `python3 verify_coloring.py` and `python3 verify_partition.py` under Python 3 using the standard library. Compare stdout to `verify_coloring.out` and `verify_partition.out`, respectively. The first script tests all 24 graph edges, verifies regularity and triangle-freeness, explicitly constructs all open-neighborhood simplices, tests the listed integer 2-cycle's full boundary, enumerates exactly all proper three- and four-colorings, checks every coloring degree against the tetrahedron's four oriented faces and BFS-exhausts both components. The second starts from the independent full neighbor-mask representation, enumerates all independent masks and 751 independent partitions, expands all 24 label permutations, builds all one-vertex edges and performs independent disjoint-set component enumeration. The two algorithms agree on the 18024-state space and the two components of 9012 each; the second independently gives 64320 undirected edges.

The key noncomputational correctness step is that two neighboring coloring maps into the tetrahedral boundary are contiguous on the open-neighborhood complex, hence give the same integral-homology degree. The explicit opposite-degree witness proves separation; exhaustive finite searches prove there are no additional components. No external audit or infinite-family claim is implied. The full text of a potentially relevant 2022 thesis was not obtained and bibliographic uniqueness is not certified.
