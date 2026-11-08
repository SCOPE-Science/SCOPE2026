---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Increasing one positions p_i satisfy upper-gap and boundary bounds against 0^r plus lower long-difference bound p_{i+s−1}−p_i>=s against 1^s. Every condition is a difference inequality preserved by componentwise meet/join. For feasible z<=p, a blocked decrement of p_i requires an eligible neighboring coordinate i−1, i−s+1, or i+1; forward blockers cross exactly r-gap barriers, while backward blockers cannot cross them when r>=3, so the dependency graph is acyclic and admits a legal decrement. Descent from each state to the meet yields an L1 shortest path; three-way coordinate median is uniquely feasible. Symbol swap covers r=2,s>=3; (2,2) is disconnected at n=4,k=2. Independent bitmask BFS checked 21,856 word pairs in 117 sectors up to n=8.

## originality

PASS

Best-of-knowledge statement/implication comparison finds no inspected stronger result covering the full final claim; known components and related earlier theorems are credited. This is not a novelty certificate.

## value

PASS

A structural classification of physically legal sorting paths under two simultaneous forbidden-run constraints, with a universal exact geodesic metric, median operation, connectivity and sharp forbidden boundary. It is a natural answer in token sliding/lattice-path reconfiguration, not a chosen finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
