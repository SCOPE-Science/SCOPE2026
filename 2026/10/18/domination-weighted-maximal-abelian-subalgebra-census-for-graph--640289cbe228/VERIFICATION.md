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

The standalone `verify.py` uses Python standard-library modules only. Run `python verify.py` from a folder containing the embedded script. It enumerates every RREF subspace, tests all edgewise brackets, computes the Lie centralizer rank, and requires maximal-abelian agreement with a separately enumerated domination formula.

Exact field arithmetic is implemented for orders \(2,3,4,5\), with \(\mathbb F_4\) represented by \(\mathbb F_2[z]/(z^2+z+1)\). For each order the program tests all \(75\) graphs on at most four labeled vertices, totaling \(300\) graph-field checks. The observed summary is `ALL_GRAPH_LIE_MAXIMAL_ABELIAN_CHECKS_PASSED 300`.

Further counts at \(q=3\) are `STAR_K_1_3 {1: 27, 3: 1}` and `COMPLETE_K_4 {1: 40}`; keys are dimensions above the central edge space. The formula for arbitrary graph sizes and fields is established by the coordinate-proportionality and self-centralizer proof in RESULT.md, not by finite enumeration. No independent mathematical audit has been performed.
