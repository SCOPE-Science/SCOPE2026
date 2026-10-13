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
# Reproducibility and scientific boundaries

Place both bundled source files `verify.py` and `orbit_test.py` in the same directory. With Python 3, execute:

```sh
python3 verify.py
python3 orbit_test.py
```

The exact success markers are `VERIFY_OK` and `ORBIT_OK`. These computations independently evaluate the operator equation and orbit action, not merely a symbolic rearrangement of the final closed forms. The direct exhaustive operator census uses \((n,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\). Orbit transitivity is exhaustively checked for \((2,2),(2,3),(3,2)\). Selected outputs: \(16\) weight-zero operators for \(n=2,q=2\) (six having nonzero square); \(33\) operators for \(n=2,q=3\); and \(176\) operators for \(n=3,q=2\) (84 having nonzero square). Direct orbit enumeration finds five, four, and six orbits, respectively.

All finite experiments are corroboration only; the general field classification, Gaussian-binomial counting, and orbit-transitivity proof are fully mathematical and do not rely on sampling. Prime-power extension fields are included by field-linear arguments, but the included programs enumerate only prime fields. The independent audit has not been performed.
