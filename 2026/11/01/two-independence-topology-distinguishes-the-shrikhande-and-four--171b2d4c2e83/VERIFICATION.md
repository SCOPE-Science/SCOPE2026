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

# Reproduction and finite verification

Run `python3 verify_two_independence.py` with standard Python 3 and no external packages. The embedded file `verification_output.json` was produced by the program as run on the complete finite domain.

The program enumerates all \(65536\) vertex subsets for each of the two distinct sixteen-vertex graph presentations. It compares two independent membership criteria for every subset: all induced connected components have at most two vertices, and no connected induced triple is present. It independently verifies strongly regular parameters, local-neighborhood connected components, all facets through the face enumeration, the exact deterministic matching, every one of \(4224\) rook and \(4960\) Shrikhande covering incidences, and directed Hasse acyclicity by complete topological sort.

Rook: \(1192\) nonempty faces; \(542\) matching pairs; critical cells \((1,1,106)\) in degrees \((0,2,3)\); exact boundary coefficient distribution \((-1:8,0:82,+1:16)\). Shrikhande: \(1336\) nonempty faces; \(638\) matching pairs; critical cells \((1,1,58)\); exact boundary coefficients \((-1:10,0:43,+1:5)\). The degree-one witnesses for critical three-face bitmasks are \(360\) and \(340\). Mod-two simplicial boundary ranks are separately computed from face matrices rather than the Morse chain complex.

The verified marker is `SHRIKHANDE_ROOK_TWO_INDEPENDENCE_OK`. The enumerations exhaust both stated finite graph complexes, but cannot themselves certify any larger family or absolute novelty. The sphere-wedge deduction also invokes Forman's acyclic-matching theorem and the CW mapping-cone argument; no independent external validation was performed.
