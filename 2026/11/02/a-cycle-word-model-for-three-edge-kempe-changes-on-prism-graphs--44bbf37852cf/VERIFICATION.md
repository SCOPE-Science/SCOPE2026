---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A direct derivation of the state bijection uses upper and lower rim words x,y: the rung has both values x_(i−1) XOR x_i and y_(i−1) XOR y_i, so x_i XOR y_i is constant b. Properness is exactly the word constraints and x_i≠b; b≠0 forces b=3 and even alternating x. At b=0, for omitted colour c, a rim edge is in the switched colour pair iff x_i≠c and a rung is in the pair iff exactly one of its two bounding rim letters is c. The pair subgraph is consequently exactly the cycles formed by runs and their bounding rungs, or the isolated upper/lower rim cycles if c is absent. A run cycle avoids the fixed vertex iff it avoids both end positions; the lower rim switch in the absent-colour case produces b=3. At b=3 the two rim matchings of either colour 1 or 2 are complementary, so that colour with the rungs forms a single alternating Hamilton cycle through u_0. Only the 1,2 lower rim switch is allowed there. The triangle-free property follows from the cited general proposition; directly, two moves at one colouring with different colour pairs already force different swap pairs on the edges on which the two outcomes differ, and distinct moves with the same pair change disjoint components, not one component. Independently checked all ten witness moves by their changed intervals: the 0-based (left,right,omitted colour) triples are (2,3,2),(1,2,1),(3,3,2),(2,2,3),(1,1,1) and (4,4,2),(2,2,2),(3,3,3),(2,4,2),(3,3,1). Each is internally bounded by the omitted colour, so the prefix leaves each move valid. For n=3 the only word is 132; for n=4 the words are 1212,1232,1312, with the latter two adjacent only to 1212; the extra leaf gives the claw. The supplied scripts were inspected, not run.

## originality

PASS

The 2017 article contains precisely the fixed-vertex formulation, the generic triangle exclusion, and a crossed-prism classification. Its remarks on ordinary prisms report small cases and the difficulty of exact form, not the claimed adjacency theorem. Ordinary-prism uniqueness of the edge-Kempe class is also known. Neither those results nor retrieved records about other cubic graphs give the full ordinary-prism word correspondence or the uniform five-cycle witnesses.

## value

PASS

A full move-preserving model for an established reconfiguration graph answers a more useful question than its size or connectivity: it permits adjacency to be read directly from a cyclic word for every rim size. The explicit five-cycle families and uniform parity-dependent exceptional leaf give concrete global information beyond finite enumeration and distinguish the ordinary family from the known crossed-prism structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
