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

# Reproducibility and scope

The exact mathematical input is the production-normalized finite radiation law as specified in RESULT.md. The complete proof uses telescoping, one polynomial derivative, a quadratic discriminant, and a controlled limit. It does not require empirical fitting or random experiments.

Run `python verify.py` using a standard Python 3 interpreter from the directory containing both files. The program uses rational arithmetic for the three-destination construction and the finite normalizer, then verifies 4,200 reproducibly seeded continuous-parameter instances, derivative identities, stationary maximum formulas and the critical-boundary scaling.

The checker printed the following results on a standard Python 3 execution:

```
exact three-destination example, finite normalization: passed
4200 randomized parameter and derivative identities: passed
boundary cases and critical onset: passed
ALL CHECKS PASSED
```

## Verification limits

The checker does not establish the theorem for all positive real parameters: that scope rests on the complete analytic proof. It does not test unmodeled distance ties, finite-population individual-level stochastic realizations, departures whose distribution changes for reasons outside this law, or empirical commuting data. Historical priority and independent review have not been established.
