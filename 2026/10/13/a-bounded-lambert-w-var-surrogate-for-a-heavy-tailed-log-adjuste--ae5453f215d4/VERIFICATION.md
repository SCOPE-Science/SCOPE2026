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

# Verification record

The mathematical proof is given in `RESULT.md`. The included standard-library Python program `verify.py` independently evaluates the exact CDF and the equation represented by the Lambert-W surrogate, with no third-party computational package or imported data.

Run command: `python3 verify.py` from this directory.

Actual replay result:

```
CHECKS_PASS
universal_coverage_ceiling = 0.759707388138908
nominal_coverage = 0.99000
surrogate_VaR = 5.065497055101
true_VaR = 171.028746496526
actual_surrogate_coverage = 0.722799852432
```

Checks cover the exact achieved-coverage identity, strict undercoverage for representative shape parameters and confidence levels, exact scalar inversion and the displayed numerical example. The code uses finite floating-point bisection, not certified interval arithmetic or an exhaustive proof of the universal analytical inequalities. The latter follow from monotonicity, logarithmic inequalities, derivative computations and first-order endpoint asymptotics in `RESULT.md`. The original full-text PDF supplies the defining CDF and published surrogate; no independent publication-priority audit has been performed.
