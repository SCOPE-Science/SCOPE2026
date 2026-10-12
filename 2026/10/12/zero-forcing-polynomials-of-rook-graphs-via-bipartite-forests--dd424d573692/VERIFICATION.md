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

# Reproducibility and boundaries

Run `python3 verify.py` from a directory containing the supplied script. The program uses only Python's standard library, with no downloaded data and no randomness. Its emitted text is in `verification_output.txt`.

The verifier reconstructs rook-graph forcing by applying the color-change rule to blue cells. A distinct union/find implementation tests the predicted bipartite-forest and degree condition. These predicates agree exhaustively on nine boards through \(4\times4\), representing 70,502 initial colorings. A component-count recursion matches each forcing polynomial coefficient on those boards. Direct spanning-tree subsets verify the bipartite Prüfer leaf formulas in 5,140 tree instances, and 25 larger parameter pairs test the extremal count expression.

This is finite corroboration. The all-parameter classification and generating formulas are justified by the proof in `RESULT.md`; an exhaustive computational certificate over unbounded board sizes is neither claimed nor needed. Literature priority has residual risk from related inaccessible material. Independent audit has not been performed.
