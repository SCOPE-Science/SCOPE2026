---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For bidirected K_{2,q}, q>=6, every multipath has at most four arcs because each of two left vertices has in/out degree ≤1. Counting all admissible orientations gives f-vector (4q,6q²−4q,4q(q−1)²,q(q−1)²(q−2)) and Euler characteristic yielding B_q=q⁴−8q³+19q²−14q+1. The proof partitions faces by external arcs after six probe columns; every external face uses ≤4 external right vertices, so the four-named-external-column fiber check covers every q symbolically. Independently reconstructed and reran all 312 nonempty external patterns and every directed matching Hasse edge (8,904 tested nonempty fiber cells total); the critical profiles matched 16·71, 56·19, 24·25, 144·5, 72·1 cells in the stated sizes and every fiber topological sort succeeded. Replayed the six-column base (1,416 simplices, 623 pairs, one critical vertex and 169 three-cells) and independently checked mod-two low-q boundary ranks q=2..5. By the patchwork lemma, the global matching is acyclic and has one 0-cell and only 3-cells, so the entire q>=6 integral homotopy type is the asserted S³ wedge; low-q non-two-connectedness is exact, not timeout-based.

## originality

PASS

Best-of-knowledge originality: final statement and implication level compared to overlapping primary literature and published mathematical records, including already-known subcases. Even stronger prior path/polygon results do not contain the dense four-cycle family; the cited alternating orientation cannot imply its homotopy by a harmless relabeling.

## value

PASS

A sharp uniform two-connectivity cutoff and explicit all-q integral homotopy classification of a natural dense bidirected family; the finite symbolic certificate reduces an unbounded-parameter question to an exhaustive meaningful boundary, rather than mere small-instance tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
