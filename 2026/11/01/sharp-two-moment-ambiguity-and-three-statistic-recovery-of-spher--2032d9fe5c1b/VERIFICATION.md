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

The analytic proof uses exact spherical area coordinates, a second-moment matrix, total covariance, and a one-variable quadratic fold on the physically admissible domain. These steps support the statements for every admissible zone; simulations do not establish universal identities.

The included standalone `check_zone_moments.py` uses only the Python 3 standard library. It directly checks rational identities and the rational ambiguity witness, parameter-domain thresholds, explicit inverse formulas and comparisons, then independently generates surface-uniform points to compare empirical mean, variance and shared-endpoint covariance with the exact predictions. The numerical tests use fixed pseudorandom seeds and declared absolute tolerances. Successful execution prints `ALL_CHECKS_PASSED`.

Independent mathematical examination and empirical priority verification beyond the cited literature have not been performed.

Recorded execution of the bundled checker:

```text
EXACT_FOLD_IDENTITY_AND_SHARED_ENDPOINT_COVARIANCE_PASSED
SHARP_TWO_MOMENT_AMBIGUITY_WINDOW_AND_EXACT_WITNESS_PASSED
GLOBAL_FIXED_AREA_REVERSAL_AND_THREE_STATISTIC_INVERSION_PASSED
INDEPENDENT_SURFACE_UNIFORM_THREE_POINT_MONTE_CARLO_PASSED 7
ALL_CHECKS_PASSED
```

The random experiments use 90,000 independent three-point draws for each of seven zone shapes. Each evaluated statistic is bounded; the empirical tolerances are not a confidence theorem. The exact inverse proof covers the entire continuous physical parameter domain.
