---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The Desargues graph is the bipartite double of Petersen: ten left two-subsets, ten right, adjacent when disjoint. Every perfect matching is an admissible 10x10 bijection. Independent backtracking counted 60. Contract a fixed matching; each remaining edge is one directed arc in a ten-vertex, twenty-arc loopless digraph; alternating cycles correspond to directed cycles. A minimum deletion set hitting all such cycles equals minimum feedback arc set = 20−max over linear vertex orders of forward arcs. Exact subset recurrence over all 2^10 vertex sets computed, independently of the packaged verifier, giving 6 matchings with anti-forcing 5 and 54 with anti-forcing 6. The supplied 240-action orbit/transversal verifier source was independently read; its exhaustive definitions support exceptional size-6 involutive Petersen lifts and other orbit sizes 24,30. Finite exhaustive enumeration is a complete proof for this fixed graph, not extrapolation.

## originality

PASS

Best-of-knowledge: existing literature defines anti-forcing via alternating cycles and gives broad bounds/graph classes, whereas no inspected published source determines this Desargues-specific complete anti-forcing polynomial or which six Petersen lifts attain the lower value. The previously reported count of 60 and 6+24+30 orbit division are not claimed as new. The anti-forcing values and exceptional structural classification survive.

## value

PASS

The anti-forcing polynomial is a motivated exact invariant of a standard named 20-vertex cubic bipartite graph. It discriminates structurally distinct perfect-matching types and shows complementary cycle lengths alone do not determine anti-forcing. A complete classification for this graph is useful independently of an infinite-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
