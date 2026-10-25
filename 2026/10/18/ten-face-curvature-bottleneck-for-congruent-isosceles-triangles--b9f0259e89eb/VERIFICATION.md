---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For ten triangular maximal facets, E=15, V=7. Five unequal-length base edges pair the ten facets into five genuine quadrilaterals, giving a spherical quadrangulation Q with seven vertices and ten equal-length edges. All Q facial cycles even, hence bipartite. Its smaller class has ≤3 vertices and thus a vertex incident to r≥4 edges. At most two unequal diagonals k touch that vertex because diagonals join a same-class pair in the simple original graph. Its exact incident angle sum is kπ+(r-2k)θ. It is ≥2π for θ≥π/2 and ≥4θ when θ<π/2, giving the stated necessary nonexistence and vertex defect bound. Verified counts and case k≤2 algebraically; no sufficiency is claimed.

## originality

PASS

Georgiou 2026 provides universal eight-facet realizability and minimum face counts, not a ten-face yes/no classification; Eppstein 2021 discusses broader isosceles surface geometry and vertex-angle restrictions, but its accessible full article does not state this 10-facet bottleneck. Existence of convex examples with 8 facets cannot imply existence for exactly 10; the five-quadrilateral bipartition obstruction is a new quantified implication relative to cited sources.

## value

PASS

Face-count realizability is not monotone in the number of congruent facets. A forced nonexistence at the natural next nonminimal even count 10, with a quantified curvature bottleneck and a graph-theoretic explanation, is a motivated geometric obstruction, not a routine Euler numerical exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
