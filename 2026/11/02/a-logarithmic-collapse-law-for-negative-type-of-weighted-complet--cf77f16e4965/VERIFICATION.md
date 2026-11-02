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

# Reproducibility record

Run `python3 verify_weighted_corona_roundness.py` with Python 3.9 or later (standard library only). The checker constructs shortest-path matrices from edge lists, tests exact rational quadratic-form identities for \(m=3,4,5,6\) at four rational pendant lengths and three integer powers, then uses an independently implemented Jacobi diagonalization to assess full zero-sum inertia for 105 numerical configurations. It also compares parameter monotonicity and limiting asymptotic formulas.

Actual successful output:

```
EXACT_QUADRATIC_DECOMPOSITION_OK checks= 576
ENDPOINT_INERTIA_OK cases= 105
STRICT_MONOTONICITY_CHECK_OK
ASYMPTOTIC_DIAGNOSTICS_OK
EXAMPLE_OK m=3 t=1 threshold= 1.709511291351
ALL_WEIGHTED_CORONA_ROUNDNESS_CHECKS_OK
```

These are finite checks only. The theorem for all real \(t>0\), all integers \(m\ge3\), and all exponents follows from the complete analytical decomposition, a power-function concavity inequality and the strict-downward-propagation theorem. The asymptotic error terms are analytical, not certified by finite numerical tests. Independent scientific audit has not been performed.
