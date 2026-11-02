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

# Finite verification and analytical scope

Execute `python verify_two_speed_coupon.py` in Python 3. The included program uses only the standard library and generates exactly this output:

```
PASS: 137 deterministic assertions
Catalan-convolution, rational-race, closed-form and first-order checks passed
Checks are finite; the infinite theorem is established in the written proof
```

The program exhausts balanced fast arrival words up to group size seven, checks the first-hit Catalan convolution, compares independently constructed rational recursions for labelled and grouped clocks, verifies the equal-rate Catalan baseline and the exact two-plus-two-clock closed formula, and checks perturbative values. It also evaluates finite large-group ratios without claiming a uniform error. The analytic arguments in `RESULT.md`, not an assertion count, prove all quantifiers. The rates, independence assumptions, right-limit order and non-uniformity of the remainder are explicitly scoped.

The scientific review is self-review only. Independent mathematical and historical-priority validation have not been performed.
