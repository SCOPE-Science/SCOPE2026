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

Run `python3 verify_tree_halfspaces.py` using standard Python 3; no external packages or input files are required. The program enumerates each labeled tree of order \(2\) through \(8\) exactly once using Prüfer sequences, groups them by a canonical rooted-parenthesis representation of their unrooted isomorphism class, constructs the \(2n\) edge-cut halfspaces and computes their exact Littlestone rank by a full recurrence on query version spaces. A separate graph-distance implementation checks the path-of-length-four/side-distance-two motif for every shape. The program asserts that all \(23\) eight-vertex shapes and all \(262144\) labeled eight-vertex trees agree with the theorem, returning counts \(11\), \(12\), \(218400\), \(43744\). An additional path-family check covers orders \(2\) through \(14\).

Expected final markers: `EIGHT_VERTEX_MOTIF_AND_COMPLETE_LABELLED_CENSUS_PASS` and `ALL_TREE_HALFSPACE_SHATTERING_CHECKS_PASS`. The universal mathematical assertion is justified by the proof in `RESULT.md`; finite checks are not used to certify an infinite claim. This is computational reproducibility and a self-review, not an independent audit or a claim of exhaustive historical novelty.
