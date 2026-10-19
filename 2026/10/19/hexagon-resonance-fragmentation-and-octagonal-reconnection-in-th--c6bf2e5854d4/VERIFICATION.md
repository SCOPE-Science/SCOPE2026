---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite checks

The input is the explicitly listed graph \(\operatorname{GP}(12,5)\), with twelve outer and twelve inner vertices and thirty-six edges. The mathematical proposition checked is the exact perfect-matching reconfiguration structure under alternating simple cycles of six, and of six or eight, edges.

Run `python3 verify_gp.py` and `python3 verify_cayley.py` in a directory containing the provided code. The first writes `nauru_certificate.json`. It constructs every perfect matching by branching at an uncovered vertex, then computes six- and eight-cycle toggles and independently verifies these adjacencies against all 7,140 matching pairs. The second uses the star-transposition Cayley representation on twenty-four permutations and independently enumerates every perfect matching and the pairwise single-cycle differences. Both count connected components, breadth-first distances and degree distributions.

The observed totals were 120 perfect matchings, twelve simple six-cycles, fifty-four simple eight-cycles, 192 six-cycle flip edges, and 414 additional eight-cycle flip edges. Hexagon-only components have sizes 57, 18, 18, 18, and nine singletons. Both representations produce a connected six-or-eight-flip graph with 606 edges, radius four, and diameter six.

The supplied `nauru_certificate.json` stores the entire 120-state vertex enumeration and each six-/eight-cycle adjacency pair. The stdout records `verify_gp.stdout` and `verify_cayley.stdout` were created by executing their corresponding source programs successfully. The first program regenerates the certificate exactly. An independent scientific audit has not yet been performed. No computation here proves an analogous result for an infinite family of graphs.
