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

# Verification and limitations

The complete proof appears in `RESULT.md`; the executable, dependency-free checker is `verify.py`. Run `python3 verify.py` under Python 3. It uses exact rational arithmetic to compare a stationary co-rotating moment recurrence against separately integrated ordered angular four-time correlations, checks convolution with isotropic Gaussian noise, and re-evaluates the closed-form positivity and inverse-Fourier formulas over 1,532 parameter cases.

The successful run reports:

```
PASS: 1532 exact-rational model and inversion cases
Positive-kurtosis benchmark: 7/68 ; negative benchmark: -215/2714
```

Proof rather than finite enumeration establishes the universal sign boundary and inverse map. The checker neither establishes independence of earlier mathematical literature nor tests asymmetric angular laws, external forces beyond harmonic confinement, finite-sample estimation, or experimental data.
