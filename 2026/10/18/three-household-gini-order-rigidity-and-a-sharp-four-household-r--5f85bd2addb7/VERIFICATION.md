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

# Verification notes

The analytical proof of the universal claim is the endpoint-gap representation of the Gini numerator at one through three households, combined with the concave Karamata inequality on equal-total majorized profiles. That proof holds for all positive real incomes and all positive nondecreasing concave transformations. No finite computation is claimed to prove that universal quantifier.

Run the self-contained checker from this package with `python3 verify_gini.py`. It uses only Python's standard library and exact `fractions.Fraction` arithmetic. It independently computes the same Gini values from ordered weighted sums and from pairwise differences; checks every majorization partial sum; verifies the raw, top-coded and smooth exact Gini comparisons; checks the displayed rational difference; and runs 1,685 low-dimensional example transformations, plus 329 cross-check profiles.

Successful execution prints:

```
VERIFY_OK majorization=PASS raw=1/4,1/6 capped=3/20,1/6
VERIFY_OK smooth=27/1060,1/34 smooth_gap=-71/18020
VERIFY_OK independent_gini_profiles=329 low_order_transform_comparisons=1685
```

This verifies the finite witness arithmetic and supports reproducibility; it neither tests every concave function nor proves mathematical originality. No independent scientific audit or validation has been performed.
