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

On four distinct endpoints, the original Kneser graph must induce exactly two edges; this agrees with the stated four cross-intersections test. A shared endpoint fails that test as its partner is disjoint from it. I independently built compatibility by counting edges on the endpoint union, enumerated maximal compatibility cliques by pivoted Bron–Kerbosch, then took all size-seven and size-eight subcliques with deduplication. Any finite clique extends to a maximal one, and pruning only when the current clique plus eligible vertices has size less than seven is safe. The counts are 6420 and 315, the mixed size-seven count is 5580, and the anchored counts are 642 and 36. Closing all size-seven orbits by the adjacent transpositions, which generate S7, gives two size-420 monochromatic orbits, plus sizes 420, 2520, 1680, 840 and 120 for profiles (6,1), (4,2,1), (4,1,1,1), (2,2,2,1) and (1,1,1,1,1,1,1), respectively. Every eight-edge set is monochromatic; any larger mixed set would have a mixed eight-edge subset. Replay: python3 /workspace/reproduce_1.py, output /workspace/reproduce_1.txt.

## originality

PASS

The supported distinct claim is the exact size-seven mixed threshold and labeled/profile/orbit refinement for KG(7,3), not the known canonical strong coloring or the maximal size. The focused Resultary comparisons and examined primary passages do not establish equivalent coverage. The primary 2012 almost-intersecting paper remains a material access limitation, not an evidence-based prior-coverage finding.

## value

PASS

This is a sharp finite stability statement for the canonical coloring of a standard odd graph. The exact departure from the monochromatic optimum is visible at seven edges, with distinct multiplicity patterns and orbit sizes, not merely one exceptional construction or a recomputation of the maximum. The classification gives a precise benchmark for structural conjectures about large induced matchings without asserting any generalization to larger parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
