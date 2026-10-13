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

# Verification of the thermal–squeezing crossover

The normalizations and limiting claims are proved in `RESULT.md`; they are not inferred from numerical samples. The included `verify.py` uses SciPy and performs the following checks on the actual formulas: Gaussian-moment normalization for 16 pairs of thermal/squeezing parameters; an independent two-dimensional angular/radial quadrature against a one-dimensional modified-Bessel quadrature at seven pairs; the exact unsqueezed single-photon benchmark; four small-thermal-purity fixed-squeezing limits; five positive finite crossover parameters; and five sharply ordered large-squeezing coefficient values, including the limiting constant; and 20 illustrative parameter checks of the explicit universal relative-error inequality. The extracted standalone test run completed with the following output:

```text
VERIFY_OK normalization=16 direct_quadrature=7 fixed_squeezing=4 joint_crossover=5 sharp_envelope=5 relative_bound=20 kappa=0.230968177814117
```

The finite computations cannot certify the path-uniform asymptotic or exclude every possible independent result. The uniform theorem instead follows from the integral comparison with explicit bounds. The direct numerical checks use finite precision and a finite test set. Run `python verify.py` after installing dependencies from `requirements.txt`.

Self-review: passed. Independent audit: not yet performed.
