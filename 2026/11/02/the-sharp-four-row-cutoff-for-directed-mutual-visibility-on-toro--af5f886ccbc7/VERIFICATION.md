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

A shortest path takes the two least nonnegative forward displacements, so a same-fibre geodesic stays in that fibre. Three selected vertices in cyclic order obstruct the first-to-third geodesic. This proves the two-per-fibre bound and justifies the candidate reduction. Independent rectangular reachability and shortest-path BFS agree: at width 4 the five-point witness works and every size 6–8 candidate fails (2040, 816, 90 respectively); at width 5 the seven-point witness works and all 2490 eight-point candidates fail; at width 6 the eight-point witness works. The lift is an all-width proof: on a witnessing path, a forward wrap from 5 to 0 occurs precisely if the terminal column is less than the initial column. Inserting empty columns there adds exactly the necessary number of steps to the forward column distance, adds no selected internal vertex, and leaves the other displacement unchanged. The undirected value 12 follows from the (8,4) entry of Korže–Vesel Proposition 3.9.

## originality

PASS

The supported distinct claim is the complete directed four-row profile, in particular the exact first width saturating the fibre bound. The directed definition and the factor bound are background, and the undirected value is an explicitly credited comparison, not an original invariant. No inspected matching statement covers the directed profile.

## value

PASS

A four-row directed toroidal grid is a natural fixed-width product, and the sharp width for saturating its row bound is useful for comparing directed and undirected geodesic avoidance. The result classifies the whole width family, isolates two real obstructions, and gives one reusable configuration for the entire stable range, not merely a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
