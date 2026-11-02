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

The attached `verify.py` is a standalone Python 3 standard-library checker. It independently constructs graph Laplacians and computes the Crank–Nicolson matrix by exact-rational Gauss–Jordan inversion; it does not reuse the symbolic proof formulas to generate the expected graph matrices.

Run: `python verify.py`. Successful replay ends with `VERIFICATION_OK {'connected_graphs': 456, 'universal_examples': 28, 'off_diagonals': 12616, 'partitions': 86, 'threshold_brackets': 270}`.

The 456 connected graphs have symmetric integer conductances between zero and the common cap three. At the predicted universal horizon, all rows sum to one, every off-diagonal entry is strictly positive, every diagonal is nonnegative, and exact zero diagonals correspond exactly to vertices incident to maximum-cap edges everywhere. For saturated-vertex cases a larger rational step produces a negative diagonal. This checks examples, not all weighted graphs.

The 86 complete-multipartite instances enumerate nondecreasing part-size partitions up to nine vertices. Integer-square-root arithmetic encloses the asserted positive algebraic root between rational endpoints. Direct exact inversion at the two endpoints brackets a positivity loss only at vertices in minimum-size parts. Each rational-root inequality is verified exactly, not inferred from floating-point rounding. The analytic all-graph and all-multipartite statements rely on the proof in RESULT.md. No independent external validation has been performed.
