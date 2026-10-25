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

# Verification and limits

The included `verify_clique_squarefree_open.py` runs on Python 3 with only the standard library. Invoke `python3 verify_clique_squarefree_open.py` beside the other delivered research files. Its two independent paths reconstruct the open-neighborhood complex directly from product-graph adjacency and then: (i) test each proposed free-face removal against the actual current face poset, comparing the exact core with the union of edge blocks; and (ii) compute all reduced mod-two Betti numbers using exact binary elimination on simplicial boundary matrices. All \(14\) test cases pass for clique widths \(4\) and \(5\) over an edge, a path, a branching star, a branching tree, a triangle, a five-cycle, and a theta graph with multiple cycles. The script terminates with `VERIFY_OK` if all assertions hold.

The proof covers infinitely many parameter pairs and is not replaced by these finite experiments. The critical universally quantified steps are the unique-center property for vertical neighbor pairs when the base is four-cycle-free, the descending free-face collapses, the exact crown-graph interface, and the diagramwise homotopy-pushout replacement. This document does not claim checks for bases with four-cycles, lower clique widths, equivariant refinements, or an independently conducted audit.
