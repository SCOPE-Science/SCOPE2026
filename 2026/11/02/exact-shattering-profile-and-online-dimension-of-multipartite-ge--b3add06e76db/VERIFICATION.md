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

# Reproducibility and scope

Run `python3 CHECK.py` with Python 3 (standard library only). It enumerates **all** vertex subsets of each tested complete multipartite graph, rather than relying on the theorem's structural list to declare convexity. Geodesic intervals are determined by graph distances: a same-part pair has all outside-part vertices as length-two intermediate vertices; a distinct-part pair is adjacent. The independent all-subsets enumeration is compared to a separately generated partial-transversal family.

For every query-support size, the program explicitly calculates the restriction patterns of all concepts, compares shattering with the structural description, and matches the resulting coefficient counts to the closed polynomial. It independently uses the full recursive Littlestone rank of the actual hypotheses; its version-space recursion is exhaustive on each finite tested graph. Printed `rank_states` is the number of memoized states examined, not a separate proof.

Verified test profiles: `(2,2)`, `(2,3)`, `(3,3)`, `(2,2,2)`, `(3,2,2)`, `(2,2,2,2)`, `(2,2,2,2,2)`. The largest has ten vertices and 244 convex-set concepts. The expected completion line is `ALL_GEODESIC_CONVEXITY_CENSUS_CHECKS_PASS`.

No finite experiment establishes universal correctness or novelty. The universal conclusions follow from the shortest-path proof and the two-branch Littlestone induction in `RESULT.md`. No external independent audit or formal proof certification has been performed.
