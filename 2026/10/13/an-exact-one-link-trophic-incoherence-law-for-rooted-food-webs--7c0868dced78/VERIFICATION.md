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
The formulas concern a rooted out-tree of \(n\ge3\) binary food-web links with one additional nonloop link directed into a nonbasal vertex.

The embedded standalone `verify_single_edge_trophic.py` reconstructs the *entire* augmented trophic-level linear system with exact fractions for every test. Its Gaussian elimination is separate from the formula used in the theorem. All edge differences are recomputed from these independently solved levels; the two formulas, the sharp feedback bound, and the complete zero-cost-link count are checked.

Run:

`python3 verify_single_edge_trophic.py`

Expected output includes:

`VERIFY_OK`

`rooted_tree_cases 1740`

`additional_arc_cases 40322`

`acyclic_arc_cases 29303`

`feedback_arc_cases 11019`

Trees are enumerated exhaustively through six vertices using Prüfer codes with fixed root; trees of orders seven through nine are sampled reproducibly. The displayed counts are verification coverage, not a proof of validity for larger trees. The manuscript includes the independent all-orders algebraic argument.

Originality remains provisional without independent audit and complete inspection of all historical scientific literature. The calculations apply to the original prey-averaged trophic-level metric, not alternate directedness scores or ecological dynamics.
