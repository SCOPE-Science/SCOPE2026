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

# Verification

Execute `python theta4_verifier.py` (Python 3 standard library, no optional packages). It reconstructs the graph, all 45/96/46 cubical cells, the integral boundary operators and the six cycle chains. It checks zero boundaries, all 46 successive free-face pairs, connectivity of the resulting graph, the unimodular \(6\times6\) chord matrix, and all 288 images of the six generators under the 48 group automorphisms. A fresh foreground execution printed `PASS: vertices=45 one_cells=96 two_cells=46 free_square_collapses=46 graph_chords=6 integral_det=-1 group_maps=288`. The underlying graph subdivision fulfills the cited deformation-retract criterion. This verifies only the finite example, not an infinite-family assertion or independent certification.
