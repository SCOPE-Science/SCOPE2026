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

Run `python verify.py` with Python 3 and no external packages. The actual source-file run printed:

`VERIFY_OK exact_labeled_orientation_cases= 13 binomial_profiles= 56`

The program directly enumerates every labeled assignment of each edge to its center or leaf for thirteen small combinations, tests all ordered agent pairs and every removed good, and compares the count with Equation (1). The separate coefficient recurrence checks Equation (2) whenever its stable-range hypothesis holds, over \(b\in\{2,\ldots,8\}\) and \(q\in\{2,\ldots,9\}\). It also checks the three displayed low-multiplicity closed formulas on finite ranges.

The mathematical proof, rather than the finite experiment, establishes the formula for all integers \(b,q\ge2\), the exceptional \(q=3\) correction, and the large-\(b\) parity rate. These checks do not establish publication priority or extend the result to nonuniform weights, different multigraphs, or a positive-good-only EFX definition.
