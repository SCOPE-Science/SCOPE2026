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

The exact graph is the 24-root D4 polytope graph with vertices +/-e_i+/-e_j and Euclidean inner-product-one adjacency (96 edges, degree eight). By the definition of Lovasz open-neighborhood complex, every face is a nonempty subset of one of its 24 neighbor sets; independent reconstruction deduplicates the complete 5088 faces, with f-vector (24,264,960,1608,1344,672,192,24). Applying the explicit ordered 24-pivot elementary pairing to every available face yields 2519 disjoint pairs, leaving exactly one critical 0-cell, one critical 1-cell, 48 critical 3-cells. Independent complete traversal of all 22128 Hasse cover incidences after reversing matched arrows topologically sorts all 5088 faces, proving the matching acyclic (not merely a greedy cancellation log). The resulting Forman CW complex has one 0-cell, one 1-cell and 48 3-cells, with no 2-cells. All maps S2 -> S1 are null because pi_2(S1)=0, so the *integral homotopy type*, not just F2 Betti numbers, is S1 wedge 48 S3. The separate mod-2 boundary ranks 23,240,720,840,504,168,24 provide consistency only. Exact finite one-graph certification is exhaustive.

## originality

PASS

PASS: the same-graph Resultary 24-cell independence complex describes an entirely different simplicial complex. General neighborhood-box equivalences and Shukla low-degree/circulant classifications do not imply the exact degree-8 D4 root-graph wedge. No exact prior open-neighborhood 24-cell result identified; priority provisional.

## value

PASS

PASS: The exceptional self-dual 24-cell graph is a canonical high-symmetry D4 root configuration. Its open-neighborhood complex has a non-obvious mixed-dimensional integral homotopy type S1 wedge 48 S3, a natural exact topological invariant which cannot be read off from its f-vector or a known low-degree graph classification. Complete explicit Morse reduction makes the one-object calculation substantial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
