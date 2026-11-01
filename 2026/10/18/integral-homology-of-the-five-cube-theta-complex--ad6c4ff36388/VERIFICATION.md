---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The claim specifies the ordinary 32-vertex five-cube graph with xor-one-bit adjacency, its edge hypergraph, reduced integral simplicial homology and nonaugmented independence complex. Independently reconstructed every independent subset using a different exact bipartite algorithm: 2^16 choices of even vertices and then all compatible odd subsets, obtaining 254475 distinct masks and the full size vector (1,32,416,2880,11760,29856,48960,54304,44240,29920,17952,9088,3672,1120,240,32,2). Reapplied the stated parity-first stage matching, obtained 127231 disjoint pairs, exactly critical cells 1 vertex, 1 five-simplex and 10 seven-simplices with the 12 supplied masks. Constructed all other lower-facet transitions among the matched pairs, obtained 99497 arcs, and Kahn-eliminated all 127231 graph nodes with no cycles. This is exhaustive over every face, not sampling. Forman discrete Morse theorem then gives a CW model with cells only in degrees 0,5,7; there are no consecutive critical degrees, so every integral cellular boundary is zero. Therefore reduced H_5=Z, H_7=Z^10, all others 0, with no torsion. Theta equals the 32-vertex Alexander dual of the independence complex; integral Alexander duality has 29-i cohomological shift, mapping H^7 to theta H_22=Z^10 and H^5 to theta H_24=Z. No homotopy wedge or full attaching-map conclusion is made.

## originality

PASS

Best-of-knowledge originality PASS for torsion-free integral homology and the explicit acyclic matching of the ordinary 32-vertex Q5, not for the previously reported Q-Betti ranks or Alexander duality. Conant–Thistlethwaite introduce the exact cubical theta setting and known rational calculations; rational ranks alone cannot determine torsion. An independent full-document reinspection of their revised version was unavailable this run (arXiv HTML/PDF blocked, authorized Oxford returned vpn_disconnected), so the claim that their detailed 2010 table explicitly leaves integer groups open comes from the actual submitted scholarly package and remains a specific primary-reading qualification, not falsely attributed to freshly read full text. Searches across theta, Ind(Q5), Boolean 4-SAT-5, and related cube complexes found no covering theorem, subject to residual alias risk.

## value

PASS

This is a motivated exact integral invariant of the canonical ordinary five-cube edge-theta complex, historically studied through the homotopy topology of Boolean satisfiability spaces. Knowing rational Betti ranks cannot rule out finite integral torsion, and a complete acyclic Morse matching giving torsion-free integral groups is not a mere table reprint, graph renaming or normalization. The computed 12-critical-cell model supplies structural information for future examination of attaching maps without pretending to settle the full homotopy type. Its finite size is intrinsic to the object, not an arbitrary unmotivated slice; a researcher studying cube theta complexes or 4-CNF topology could reasonably need its exact integral groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
