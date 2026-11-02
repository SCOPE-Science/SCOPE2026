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
The finite-dimensional projection is defined on the full finite cube with full-support independent Bernoulli measure. The proof's critical convex-order inequality is an analytic all-dimensional argument; the finite checks below are reproducibility diagnostics, not a certificate for unbounded dimensions.

Run `python biased_first_chaos_checker.py` with Python 3 and its standard library. Output verified:

```
PASS 2286 exact full kernel rows and 4455 exact two-binomial support cases
PASS 1860 heterogeneous exact kernel rows at 150 bias profiles
```

The checker constructs all kernel entries using `fractions.Fraction`, maximizes exact absolute row sums for each finite instance, and compares them with the rare-corner expression and the closed homogeneous boundary-binomial formula. The source and its dependencies are included in full. The asymptotic consequences use standard local central-binomial and Poisson convergence theorems and are not inferred from finite numerical tests. No independent scientific verification has been performed.
