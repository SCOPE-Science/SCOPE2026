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

# Computational verification and proof boundaries

The complete source `verify_rook.cpp` is compiled using `c++ -std=c++17 -O2 verify_rook.cpp -o verify_rook` and executed as `./verify_rook`. Its recorded standard output is in `verify_rook.out`.

The checker generates rook-graph adjacency bit masks directly from row/column equality. For each nonempty subset of vertices, it tests every omitted vertex for a selected neighbor, then takes the maximum outside-neighbor count over selected vertices. It enumerates every feasible \(k\) from that count through the maximum degree and computes exact cardinality minima. For \(k<\min(m,n)\) it additionally counts all minimizers and compares with the slab-count formulas.

Fourteen boards of at most twenty squares were exhausted: the sum of examined nonempty subsets is 1,763,138, covering 93 capacity choices. All exact minima and the low-capacity minimum-set counts agree with the theorem. This is a finite cross-check, not a proof for arbitrary board sizes. The proof for arbitrary \(m,n\ge2\) and \(0\le k\le m+n-2\) is the row/column occupancy argument in `RESULT.md`.

The work does not independently verify any external paper, and makes no claim of an independent literature or mathematical audit.
