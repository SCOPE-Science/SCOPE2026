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

The accompanying `verify.py` is runnable with Python 3 and only standard-library `fractions.Fraction`. Execution returned:

```
VERIFY_OK polynomial_identities=6 exact_system_solves=48
Cramer_degree_bound=23 distinct_positive_evaluations=24
positive_root_interval=(5,6) exactly_one_by_Descartes
```

The code reconstructs the 15-by-15 transient matrices, includes the absorbing empty state through a zero continuation term, and performs 48 exact rational linear-system solves (24 rates for each of the two graphs). The rational formulas for four vertex orbits agree at all 24 rates. Since each Cramer numerator has degree at most 14 and each determinant denominator at most 15, the stated numerator/denominator degrees bound the cross-multiplied error degree by 23. Consequently agreement at 24 distinct points certifies the rational-function identities for all positive real rates. Separately, direct integer-coefficient multiplication checks six explicit difference identities; the unique crossing follows analytically from the one sign change in the displayed polynomial and exact opposite signs at 5 and 6.

No finite numerical sampling is used to infer an infinite conclusion without a degree argument. The package does not contain empirical ecological validation. The full text of DOI:10.1103/PhysRevE.92.032806 was not available for complete originality comparison; its published abstract was read and its overlap is disclosed in `REVIEW.md`.
