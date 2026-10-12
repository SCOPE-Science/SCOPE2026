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
# Verification of the exact no-isolate NODF expectation

The code file `verify_fixed_row_nodf.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Run from the directory containing this document with `python verify_fixed_row_nodf.py`. Expected output:

```
VERIFY_OK distinct_profiles 305 covered_matrices 145503 sample_profile (1, 2, 3) sample_mean 7/15 sample_count 60
```

The test enumerates labeled binary incidence matrices independently of the coefficient formula for 305 feasible sorted row-degree profiles across fifteen shapes, amounting to 145,503 covered matrices, then compares rational means. It also checks that the two-marked-column counts are nonnegative and that the positive-column coefficients sum to the inclusion–exclusion cardinality. Direct matrices are enumerated by row-subset Cartesian products; the formula is implemented as independent alternating integer sums plus dynamic polynomial coefficient updates.

The proof's all-dimensional claims follow from inclusion–exclusion and coefficient extraction, not from the finite test. The check does not prove originality, rule out source coverage, or evaluate the exact variance, full distribution, fixed-fixed ensembles or weighted NODF. Independent audit has not been performed.
