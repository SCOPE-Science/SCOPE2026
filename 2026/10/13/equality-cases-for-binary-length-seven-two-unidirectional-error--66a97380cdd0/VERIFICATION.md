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

`VERIFY.py` performs the following finite checks from definitions.

It generates every binary word of length seven and its radius-two unidirectional error ball, where all changed coordinates in one received word have the same direction. Independently, it computes the classical unidirectional distance and confirms for all unordered pairs that ball disjointness is equivalent to \(d_u\ge5\).

It constructs the complete compatibility graph, enumerates every four-clique, and checks that each has no common neighbor. Thus the exhaustive computation proves both existence of four-word codes and nonexistence of five-word codes. It then recomputes all \(1680\) equality cases, their two weight-profile classes, their directional-pair profiles and their covered-output counts.

Finally, it applies all \(7!\) coordinate permutations and global complementation to one representative of each class, obtaining disjoint orbits of sizes \(1260\) and \(420\) whose union is the full equality census. The resulting stabilizer orders are checked by orbit-stabilizer in the order-\(10080\) acting group.

The verification is finite and exact. It does not establish that the stated acting group is the full automorphism group of the compatibility graph, and it does not address lengths other than seven or error radius other than two.
