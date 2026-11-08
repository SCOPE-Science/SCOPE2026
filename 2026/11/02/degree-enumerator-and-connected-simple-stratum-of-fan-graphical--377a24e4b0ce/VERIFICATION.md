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

Every directed cycle in a fan contains a directed triangle because the underlying fan is chordal. In an acyclic orientation a directed edge is individually reversible precisely when it has no alternative directed path; chordality shortens any alternate path to a directed 2-step path. Hub spoke sign strings split into maximal same-sign runs. Between unlike signs, rim orientation is forced transitive and nonflippable; within runs, each rim edge is flippable and a spoke is flippable exactly when the associated path vertex is a source (positive run) or sink (negative run). Two-state transfer of path direction words counts source/sink occurrences and gives per-run B=tz/[1-2tz+(1-t)t^2z^2]; summing alternated runs with two initial signs yields exact rational D_n series. The H_n coefficient recurrence H_n=3H_(n-1)+(t-1)H_(n-2) gives Fibonacci 2F_(2n) min class and top coefficients. For connectivity, within-run edge flips move the marked source/sink along the rim; by moving marks toward adjacent sign boundaries then flipping a negative spoke one reduces number of negative spokes while preserving a unique mark in each remaining run. A singleton negative run between positives is handled by bringing both positive source marks to the boundary and merging around the converted site, proving connectivity of the entire min-degree stratum. Independent brute force orientations via topological sorting and direct single-edge flips for n=3..7 checked each predicted degree histogram and simple-induced BFS connectedness; this finite range is corroboration, not the n-unbounded proof.

## originality

PASS

Best-of-knowledge: actual Resultary semantic queries and primary published mathematical statements were compared by object, hypotheses and implications; no source inspected established this entire additional conclusion. The four explicit comparisons, source inspections and residual risks below qualify historical priority; inaccessible full texts alone do not count as disproof.

## value

PASS

The degree of a graphical zonotope vertex and connectedness of its simple-vertex induced subgraph are natural finer geometric/combinatorial invariants than total vertices. This gives a complete infinite-family degree spectrum and the nontrivial coexistence of a connected simple stratum with exponentially vanishing density, not implied by full flip-graph connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
