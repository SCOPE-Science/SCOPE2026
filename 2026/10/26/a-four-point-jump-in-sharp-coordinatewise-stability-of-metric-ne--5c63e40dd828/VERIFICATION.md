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

# Reproducible verification

Run `python3 verify_metric_nearness.py`. No external package or network connection is required. Exact `fractions.Fraction` arithmetic enumerates 8 three-point and 4,096 four-point triangle-normal subsets, converts every subset to a canonical rational row-echelon span, and evaluates each associated orthogonal projector's maximum absolute row sum. Assertions check symmetry, idempotence, annihilation of the selected normal basis, the complete rank tables, and upper bounds \(4/3\) and \(8/5\).

The equality witness is checked using two strictly positive inputs, feasible pseudometric outputs, explicit positive KKT multipliers, and an exact ratio of \(8/5\). All assertions in the checker completed successfully.

The proof concerns only the declared three- and four-point cases. Exact finite enumeration does not imply a bound in all dimensions. The source comparisons are scientific literature examinations and do not constitute independent priority certification.
