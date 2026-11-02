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

Run the two standalone standard-library Python 3 programs in the same directory as this document:

`python3 verify_matchings.py`

`python3 verify_edge_backtrack.py`

Both programs terminate with assertion failures if a count, membership relation, distance profile, factor-cycle signature, graph parity condition, or component statement is violated. The first constructs all 33 perfect matchings of \(GP(8,3)\) by complete recursion and assembles all 120 ordered three-colourings and their 342 distinct Kempe edges. It independently generates a 96-element graph-automorphism group from four printed permutations, verifies its regular action on the larger component, and checks six involutory neighbour generators. The second constructs the full 120-state set by a different direct edge-colouring recursion and independently derives the Kempe relation and shortest-path distributions, including an explicit simple odd cycle of length five in the smaller component.

The tested bounds are finite and exhaustive: sixteen graph vertices, twenty-four edges, three named colours, 120 colourings and every legal pair-colour alternating cycle. Shortest paths are computed over each entire component, not sampled. These scripts do not establish statements about other graphs or statistical mixing times. External scholarly validation has not been performed.
