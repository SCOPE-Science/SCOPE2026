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

## Reproducible arithmetic checks

Run `python3 artifacts/verify.py` with an ordinary Python 3 standard-library installation. The script uses exact rational arithmetic to independently solve each finite absorbing Markov-chain system for the bounded joint generating function and compares it with the stated recurrence. It separately enumerates finite first-passage histories to check Catalan coefficients; checks the exact ceiling-tail formula; and evaluates finite-parameter height crossovers near the critical parameter.

Expected success lines:

```
EXACT_CATALAN_HEIGHT_AND_GENERATING_FUNCTION_CHECK_OK
FINITE_SCALING_CHECK_OK
```

## Limits of verification

Finite arithmetic checks establish consistency only for their enumerated parameters, ceiling bounds, and time horizons. The unrestricted distributions, first-passage height identities for all parameters, and asymptotic critical crossovers are proved analytically in `RESULT.md`. The optional-stopping step uses a finite-state exit with a geometric overshoot of finite exponential moment. Publication priority beyond the inspected literature, and independent mathematical audit, have not been established.
