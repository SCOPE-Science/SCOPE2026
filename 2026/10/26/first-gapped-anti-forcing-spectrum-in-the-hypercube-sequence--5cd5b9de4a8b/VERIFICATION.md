---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For each dimension the least-unmatched-vertex recursion exhausts perfect matchings without duplication. The Q4 count 272 also agrees with an independent eight-by-eight bipartite permanent recursion. To leave a matching unique after deleting nonmatching edges is exactly to hit every M-alternating cycle. Orient even-to-odd nonmatching edges and contract the matched edges: alternating cycles correspond to directed cycles. The maximum arcs retained acyclic equals the maximum forward arcs in a topological order, computed exhaustively by an exact subset recurrence on eight vertices. Independent matching enumeration and independent feedback-order DP reproduced the full Q1..Q4 spectrum and Q4 multiplicities; exhaustive competing-matching tests gave ordinary forcing number 4 for all 272. The 384 coordinate permutation/translations exhaust Aut(Q4), partitioning matches into eight orbits; the package verifier checks all 8! orders on one representative per orbit. This is a complete finite proof, with no claim about d>4.

## originality

PASS

Best-of-knowledge statement-level comparison, with specific primary-source inspections, previously covered components credited, and residual overlap risks. Retrieved search results alone are not evidence of novelty.

## value

PASS

Perfect matchings of hypercubes are canonical forcing/anti-forcing objects, and identifying the earliest noninterval spectrum is a natural sharp finite boundary. The full submaximum polynomial and eight symmetry orbit refinement distinguish configurations with the same direction multiplicities but different anticforcing behavior. The value is not claimed to arise merely from the previously known maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
