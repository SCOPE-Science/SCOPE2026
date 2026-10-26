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

The included `verify_ageing_rates.py` is a standalone Python-standard-library calculation. Run it as `python verify_ageing_rates.py` from a directory containing the packaged file. It checks five rational-parameter exponent/moment boundary cases and computes four finite-stage survival probabilities by the exact nonnegative spectral integral at initial site one.

Actual output:

```text
alpha=2/5 beta=0 delta=0 n=200 survival=0.0013658415675 normalization=565685.425 ratio_to_stable_limit=1.00707451
alpha=2/5 beta=1 delta=0 n=200 survival=0.000146563378025 normalization=49187498.1 ratio_to_stable_limit=1.00768923
alpha=1/3 beta=1 delta=-3 n=300 survival=0.00028786689189 normalization=17506095.7 ratio_to_stable_limit=1.00636390
alpha=1/3 beta=1 delta=-2 n=300 survival=0.000120071351244 normalization=100640214 ratio_to_stable_limit=1.00645382
CHECK_OK exact_parameter_cases=5 spectral_quadratures=4
```

The finite quadratures confirm the normalization trend to within the prescribed tolerance. They are **not** an infinite-time proof. The proof is the Bessel-kernel identity, weighted-alpha stable convergence, uniform negative-moment bound, and deterministic regularly varying clock inversion in the main result. No independent audit or independent validation was performed. Broader literature identity under other terminology is not ruled out categorically.
