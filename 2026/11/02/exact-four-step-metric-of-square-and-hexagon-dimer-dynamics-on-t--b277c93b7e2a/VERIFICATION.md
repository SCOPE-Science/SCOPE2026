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

All perfect matchings of Q4 are captured exactly once by assigning each of eight even vertices a distinct odd neighbour. Two perfect matchings are adjacent precisely when their symmetric difference is one connected alternating 4- or 6-cycle: the component is 2-regular on 4 or 6 vertices. A separately written all-pairs test enumerated 272 matchings, 768 square and 1216 six-cycle edges. All-source BFS reached all 272 vertices and independently recovered unordered pair histogram {1:1984,2:10784,3:19568,4:4520}, sum 36856, and eccentricity 4 at all 272 sources. Exhaustion is rigorous because every perfect matching is a unique even-to-odd bijection and every move is characterized by the symmetric difference. The result is exactly for labelled Q4, not higher-dimensional dimer dynamics.

## originality

PASS

Best-of-knowledge new sharp full Q4 4-or-6-cycle move metric and self-centered eccentricity, distinctly not the known 272-state total or square-only graph components; exact finite data could have unindexed historical duplication.

## value

PASS

The first genuinely four-dimensional hypercube exhibits eight square-flip frozen states, so the complete metric after adding the smallest useful non-square alternating switches is a motivated local-move invariant. Exact radius, diameter, edge types and all-pairs distances determine optimal reconfiguration costs rather than a trivial isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
