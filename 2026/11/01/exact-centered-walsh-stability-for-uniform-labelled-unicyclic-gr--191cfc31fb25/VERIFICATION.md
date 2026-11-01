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

The standalone `check_unicyclic.py` was executed using standard Python and exact `fractions.Fraction` arithmetic. For each \(n\in\{4,5,6,7\}\), it enumerates all \(n\)-edge subsets of the complete simple graph, tests connectivity, and checks the full inclusion-moment table against the stated formulas. It also verifies one explicit nonzero vertex-star eigenvector and one independent four-edge-interaction eigenvector by exact matrix multiplication. Its observed unicyclic counts are 15, 222, 3660 and 68295, respectively, agreeing with the forest count.

These finite experiments are not a proof for unbounded \(n\). The mathematical proof uses a weighted rooted-forest matrix-tree determinant, exact cycle-length moments, Johnson algebra diagonalization and elementary inequalities; all steps are written in `RESULT.md`. No independent reviewer or external certification has examined the result.
