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

The bundled `check_period_five.py` is a standalone Python 3 program requiring no third-party packages. It exhausts \(3^n-1\) nonzero symbolic words at every length \(1\le n\le5\) using exact rational arithmetic. The program derives the unique affine periodic response, computes all strict active and closed neutral admissibility inequalities, and compares the resulting classification with the four canonical five-word classes and their stated intervals. It verifies exact closure in the original physical recurrence, the two-cycle symmetry, and the exclusion of the grazing endpoint. It then tests six distinct rational parameters in the general attracting-family formula.

The result's algebraic proof independently derives uniqueness of the affine response and the strict domain criteria, and proves the open parameter interval and local attraction. The exhaustive finite checks do **not** certify any longer-period classification. All reported checks are reproducible from the supplied program and the embedded scientific formulas. No external independent review or validation was performed.
