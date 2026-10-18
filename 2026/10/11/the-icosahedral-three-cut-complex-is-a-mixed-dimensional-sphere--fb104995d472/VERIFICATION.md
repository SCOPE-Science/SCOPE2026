---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Starting from the actual package 30-edge icosahedral graph, independently checked 12 vertices of degree 5 with each open neighborhood an induced 5-cycle; exactly 140 of its 220 three-vertex induced subgraphs are disconnected (≤1 internal edge). Complements give 140 nine-vertex facets, exactly 3906 nonempty faces and f=(12,66,220,495,792,924,792,465,140). Reconstructed the 1949 matched face-poset cover pairs in stated toggle order; verified all 22800 covers and a full acyclic directed Kahn sort, leaving precisely one 0-, one 7- and six 8-dimensional critical cells. Independently computed combinatorial Alexander dual K with f=(12,66,80,30), and EXACT signed rational boundary ranks (11,49,30), giving cohomology rank6 in degree one. Alexander duality on 12 vertices yields Q-top homology rank6 in degree 8 for cut complex. Since six critical 8-cells map to only one critical 7-cell, rational boundary rank must be zero and thus the integer cellular differential is identically zero. Attaching maps S7→S7 are degree-zero and nullhomotopic, proving integral S7∨6S8 (not merely the rational Betti sequence). The pure 8-complex has nonzero H7 so cannot be shellable. This is a finite exact proof for the specified graph and parameter.

## originality

PASS

Neither Bayer et al. primary k-cut graph-family classifications nor the sequel includes the icosahedron or determines its mixed S7/S8 wedge. A separately published cuboctahedral three-cut theorem has coincident sphere multiplicities for a nonisomorphic graph but DIFFERENT f-vector and 3-cut facets and does not imply the icosahedral result.

## value

PASS

PASS: A twelve-vertex five-regular Platonic graph with twenty triangular faces is a canonical triangle-rich three-cut benchmark outside chordal and complete-skeleton shellability regimes. A pure eight-dimensional simplicial complex with actual adjacent-degree homotopy S7∨6S8 supplies an explicit integral NONshellable case with a genuinely natural graph and cut parameter. The exact full homotopy type and Alexander duality certificate, not a matching number by coincidence with another graph, constitute the mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
