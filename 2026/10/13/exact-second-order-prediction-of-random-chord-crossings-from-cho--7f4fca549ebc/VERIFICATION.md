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

The file `verify.py` is included in full. Its symbolic checks derive the pair-crossing moments from the density of the short-arc fraction, verify conditional-kernel first and second moments and the strict formulas for both variance components, and rederive their exact explained fraction algebraically for symbolic size. It constructs independent rotations of geometrically specified chords and computes genuine circular crossing indicators, rather than sampling the analytical Bernoulli kernel.

The executed program returned:

```
fixed_radii 2 mean 0.22026 target 0.22 variance 0.17174 target 0.1716
fixed_radii 4 mean 1.82588 target 1.82 variance 1.06355 target 1.0628
fixed_radii 3 mean 0.83796 target 0.84 variance 0.56271 target 0.5664
iid_chords 3 cross_mean 1.00003 theory 1.0 cross_var 0.8003 theory 0.8 pred_var 0.29901 theory 0.3
iid_chords 6 cross_mean 4.99292 theory 5.0 cross_var 5.99092 theory 6.0 pred_var 3.50022 theory 3.5
VERIFY_OK symbolic=8 conditional_samples=3 unconditional_samples=2
```

Environment: Python 3 with SymPy and NumPy. Reproduce with `python verify.py`. Numerical sampling tolerances are intentionally nonzero, are listed in the code, and do not establish an all-sample-size theorem. The proof uses conditional rotation symmetry, pairwise conditional independence of crossing indicators, exact integration, and the law of total variance; those steps are independent of the experimental checks. No human or external independent audit was performed.
