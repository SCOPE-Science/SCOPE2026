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

# Reproducibility and checks

The derivation is mathematical: classify the two-deletion forests, use the Gram determinant \(s(n-s)\), then prove the sharp bridge and cyclic concavity inequalities. The accompanying `CHECK.py` evaluates all connected unlabeled simple unicyclic graphs in the NetworkX graph atlas on four through seven vertices (53 graphs), all leaf allocations for \(3\le c\le6\) and \(1\le n-c\le7\) (28 parameter groups), their stability defects, and eight independent convex-hull surface-area/volume computations (when SciPy is available). The script does not supply an infinite proof. Floating-point tolerance is stated in the code; the displayed analytic inequalities are exact.

No independent mathematical audit has been conducted. External-source overlap comparisons are limited to the inspected references and identified prior records; exhaustive originality is not claimed.
