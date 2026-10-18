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

# Verification of the claimed classification

The proof in `RESULT.md` establishes all infinite and sharp claims: in a graph with the stated local quotient, the low-degree cell is a matching; the induced cycles from contracted multigraph cycles force a tree; the local degree equation forces the leaf triangles; and deleting the leaves recovers the subcubic core. The direct construction and tree degree sum verify the counts. Color refinement stabilizes after the degree split, and equal cell sizes imply the same \(C^2\) invariant. The two four-vertex core tree shapes give the sharp restricted forty-vertex collision; spiders yield arbitrary multiplicity.

Run `python3 verify.py` using Python 3 without third-party packages. The program asserts the quotient degrees and numerical sizes, intrinsically reconstructs the tree by contracting low-degree matching pairs, checks every biconnected block is a clique using an edge-stack decomposition, and computes color refinement for the nonisomorphic forty-vertex pair simultaneously. The example is nonisomorphic because its recovered internal core has maximum degree two in one graph and maximum degree three in the other. The script verifies 35 constructed finite instances, including core orders one through four and thirty path cores. An additional separate finite consistency experiment examined 46 unlabeled subcubic trees through order nine.

These are independent *computational routes for finite test cases*, not an independent audit of the mathematical result. They neither enumerate all infinite instances nor establish bibliographic novelty. The infinite classification, sharp cutoff and spider family depend on the explicit proof. Independent validation remains unperformed.
