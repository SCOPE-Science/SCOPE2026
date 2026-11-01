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

# Reproducibility and verification

The analytical verification consists of five exact steps: substitution into the fixed-point formula; differentiation of the arctangent; inversion of the \(2\)-cycle implicit system whose determinant is \(5\); the exact matrix trace identity \(7+3(d_a+d_b)+d_ad_b\); and the Taylor coefficients of the traces. Both displayed quadratic coefficients are strictly positive because \(25>7\sqrt5\). Differentiating a hypothetical \(C^1\) conjugacy at a primitive period-two orbit would preserve its two-step derivative trace, in contradiction with the calculated deviation from \(7\).

Run the standalone Python 3 program `verify_periodic_data.py` directly in the same directory as this document. It has no nonstandard dependencies. On the checked execution it printed:

```
branch 0.8 0.2 coefficient 4.673762078751 verified
branch 0.6 0.4 coefficient 20.326237921249 verified
mu=0.01, traces 7.000467346768 7.002032773233
all numerical checks passed; asymptotic universality is proved analytically
```

The script evaluates the exact fixed-point cancellation for seven perturbations, checks two lifted primitive two-cycles at five perturbations each, tests the first-order orbit corrections, and compares quadratic trace asymptotics at finite positive perturbations. These computations are diagnostic only; they are not an exhaustive check over the continuous parameter interval. The proof itself does not give a globally sharp perturbation cutoff. Independent mathematical review has not been performed.
