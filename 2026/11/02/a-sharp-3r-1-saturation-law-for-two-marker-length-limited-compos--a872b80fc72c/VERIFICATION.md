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

This package includes `verify_two_marker_limited_deck.py`, executable with ordinary Python 3 and no external dependencies. Its literal window enumerator computes weight-composition counts from actual words independently of the gap-polynomial proof. It compares every observation class with the proposed truncated-gap signature in both directions, checks the complete finite-length capacity formula, verifies the two generating-polynomial identities by coefficient arithmetic, and checks the saturation formulas at larger parameters.

Executed output:

```text
VERIFY_OK literal_source_profiles=50050 length_cutoff_pairs=324
VERIFY_OK every_literal_profile_matches_complete_signature=True
VERIFY_OK both_exact_generating_polynomial_identities=True
VERIFY_OK full_finite_length_formula=True saturation_and_boundary=True
VERIFY_OK symbolic_formula_large_r=1..119
r=1 saturated_capacity=1 first_saturated_length=2
r=2 saturated_capacity=5 first_saturated_length=5
r=3 saturated_capacity=12 first_saturated_length=8
r=4 saturated_capacity=22 first_saturated_length=11
r=5 saturated_capacity=35 first_saturated_length=14
r=6 saturated_capacity=51 first_saturated_length=17
r=10 saturated_capacity=145 first_saturated_length=29
```

No experiment proves the infinitely many cases. The general proof is the polynomial/truncation argument and disjoint counting in `RESULT.md`. Checks do not cover noisy reads, altered weights, cyclic words, or unobserved source errors. External independent scientific audit has not occurred.
