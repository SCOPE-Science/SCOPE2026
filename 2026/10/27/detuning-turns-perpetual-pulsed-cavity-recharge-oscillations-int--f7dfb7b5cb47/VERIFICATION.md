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

# Reproducibility

The included `verify.py` uses Python, NumPy and SciPy. Run `python verify.py` from the extracted package directory. The test output was:

```
matrix_vs_analytic: 300 tests PASS
envelope_post_cutoff: 80 tests PASS
detuning 0.1 maxima 26 scaled 2.6 target 2.46304657 relative_error 0.0556
detuning 0.05 maxima 50 scaled 2.5 target 2.46304657 relative_error 0.015
detuning 0.02 maxima 124 scaled 2.48 target 2.46304657 relative_error 0.00688
detuning 0.01 maxima 247 scaled 2.47 target 2.46304657 relative_error 0.00282
all checks PASS
```

Numerical comparisons match exact matrix propagation and derivative root brackets for finite parameters. The proof of infinitely many resonant peaks, finite peaks at every nonzero detuning, and the bounded-remainder asymptotic is analytic and is not replaced by a finite test suite. No independent scientific audit has been performed.
