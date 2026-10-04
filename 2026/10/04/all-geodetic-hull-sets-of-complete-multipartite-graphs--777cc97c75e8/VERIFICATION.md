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

The proof uses the literal shortest-path definition of geodetic convexity. In a complete multipartite graph, distinct vertices in different parts are adjacent, while distinct vertices in one part have distance two and every vertex outside that part is a possible middle vertex of a shortest path. This gives the exact one-step interval formula used in the proof.

The bundled `verify.py` independently constructs each complete multipartite graph from its part profile, computes all-pairs distances by breadth-first search, iterates the shortest-path interval operator for every subset, and compares the resulting hull predicate with the theorem. It then checks every coefficient of the three-case enumerator and the minimum hull-set size.

The exhaustive range is every nondecreasing part profile of total order from two through nine with at least two parts. Replay result:

`VERIFY_OK profiles=87 subset_checks=22932 hull_sets=12835 coefficient_checks=728 minimum_checks=87 max_order=9`

The finite enumeration is a stress test only. The unbounded theorem is established by the symbolic interval argument in `RESULT.md`.
