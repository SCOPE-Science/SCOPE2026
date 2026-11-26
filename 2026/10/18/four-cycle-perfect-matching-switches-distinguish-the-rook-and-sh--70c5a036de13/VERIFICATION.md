---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A fresh enumeration from the two stated host graphs grouped the eight-edge perfect matchings by their six-edge subsets. Distinct matchings sharing six edges differ in exactly two different pairings of the same four vertices, hence in precisely one alternating four-cycle. All-source BFS on this alternative construction verified R: 2016 states, 6048 switches, component sizes 1368, 288 twice, and 72 isolated; S: 1920 states, 5280 switches, component size 1908 and 12 isolated. The radii/diameters (7,8), (14,14), (10,13), and all 576 degree-three vertices in the two 288 components were reproduced. The direct rook isolation proof also checks: exactly one horizontal edge per row and one vertical per column are necessary, horizontal pairs form an assigned C4 on the columns, and complementary incident-row pairs give distinct vertical pairs. Mixed pairs cannot switch: if the horizontal row meets the vertical edge, the needed same-column horizontal vertex would coincide with its endpoint; otherwise both horizontal vertices would need the vertical column.

## originality

PASS

The move and graph pair are standard. No earlier theorem or exact catalogue entry checked determines the complete numerical component and distance profile for this switch operation on these two hosts. In particular the closely related records either change the states, the move, or the host.

## value

PASS

Rook and Shrikhande are the canonical same-parameter nonisomorphic pair. Their complete switch profiles give a concrete witness that those parameters do not control the frozen states or the exact distances in this natural reconfiguration process. The two cubic diameter-14 rook components and the single large Shrikhande component are more informative than simply observing that both switch chains are disconnected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
