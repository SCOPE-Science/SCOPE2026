---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The five listed families A_i..E_i are minimum triples under standard forcing, and pairwise two-element intersections yield a 5m-vertex, 11m-edge adjacency graph. Inspected complete verification/cover_distance_table.json and verify_gear_metric.py: the explicit infinite-cover potential satisfies zero only at source, nonnegative Bellman unit-Lipschitz neighbor bounds and a descending neighbor, which characterizes exact distance; linear parity tails permit finite branch checks for every integer displacement. Quotient distances minimize over translates, nearest-two suffice by tail monotonicity, and band/boundary inequalities give eccentricity recurrence e(m+4)=e(m)+3 beyond four base classes. Independently rebuilt adjacency and BFS distances for every m=4..80, all five types; matched floor((3m+3)/4) radius, floor((3m+6)/4) diameter and C/E exception. Unbounded result rests on symbolic tail induction, not finite BFS alone.

## originality

PASS

Best-of-knowledge PASS for full labelled token-jump eccentricity metric for gear graphs; the 2020 source defines the reconfiguration graph and the 2024 paper supplies minimum forcing three/propagation properties, not the 5-class distance formula. No Resultary exact gear-reconfiguration metric was found in search.

## value

PASS

Exact farthest-set geometry for a canonical reconfiguration family, determining accessibility and center/periphery by state type for all graph sizes, not merely counting minimal sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
