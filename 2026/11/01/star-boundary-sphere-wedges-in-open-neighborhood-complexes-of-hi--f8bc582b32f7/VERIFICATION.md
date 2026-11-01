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

# Verification and reproducibility

Run `python3 verify.py` using the Python 3 standard library. The script independently constructs both the actual open-neighborhood complex and the predicted relative-collapse target from graph edge lists. It verifies the graph hypotheses, reconstructs all neighborhoods directly, verifies unique ownership of all mixed pairs, checks every requested collapse against **all remaining faces** (not only local faces), checks that the final face set equals the target, and independently computes reduced simplicial mod-two boundary ranks.

The six finite inputs cover the Petersen graph, Heawood graph, the incidence graph of the projective plane of order three (original, one edge removed, two disjoint edges removed), and a bridge-joined Petersen/plane graph with vertices of degree three, four and five. The verified totals are 11,766 augmented faces and 5,062 elementary collapses. The final output line must be `EXACT_GLOBAL_COLLAPSE_AND_MOD2_HOMOLOGY_OK examples=6 faces=11766 collapses=5062 boundary_checks=2`; complete expected output is in `verification_output.txt`.

Two additional intentionally out-of-scope short-cycle graphs, \(K_4\) and \(K_{3,3}\), are checked to show that blindly extending the formula to triangles or quadrilaterals gives wrong answers. The finite calculations verify six explicit instances and the functionality of the symbolic collapse construction there. The universal statement is proven separately by the unique-generating-edge argument and the blockwise free-face collapses, followed by the graph-of-spaces homotopy reduction. No computer experiment is treated as an exhaustive proof of infinitely many graphs. No independent audit or external certificate is claimed.
