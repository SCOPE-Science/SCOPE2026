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

# Reproduction notes

The proof in `RESULT.md` establishes the continuous parameter and all-time assertions. A numerical program `verification/check.py` independently checks the finite calculations in Python 3 with packages `mpmath` and `scipy`:

```
python verification/check.py
```

The execution completed successfully and printed: `PASS: 66 independent checks; all limiting/strict statements proved analytically.` Tests include the stationary Fourier-resolvent jump and normalization, heat-kernel covariance quadrature, differentiation and integration of the erfc formula, the Laplace-transform resolvent and its zero-frequency constant, and independent nested integration in physical variables and multiple parameter settings. Numeric tolerances are specified in the program.

**What numerical execution does not establish:** it neither proves sign at every real lag nor checks infinitely many values. Those statements rest on the independent-copy strict opposite-monotonicity argument and exact resolvent integration in the proof. All assumptions are strictly positive diffusivities and reset rate, with equilibrium initialization.

No experiment, external mathematical certification, or independent audit is represented here.
