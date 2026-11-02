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

Run `python3 verify.py` from a directory containing the supplied file, with Python 3 and no third-party packages. The verifier exercises an exactly constructed eight-state Markov generator, rational-polynomial identities, the explicit quartic at the directed-cycle endpoint, the unique bias-root calculation, parameter-regime checks, and near-threshold peak scaling. The replay output was:

```
PASS: 783 deterministic exact and floating-point checks
drive tricritical ratio squared s* = 0.910181756256864
drive tricritical ratio = 0.954034462824517
directed-cycle onset u* = 0.628329993039018
directed-cycle tie frequency omega/a = 0.342295845208204
```

The analytic proof in `RESULT.md` establishes positivity, global comparisons, uniqueness, all parameter regimes and limiting exponents. The code is a finite verification aid: its test cases are not an exhaustive proof or an independently certified result. The root values shown are floating-point approximations, not exact declarations. The source spectrum and model are credited to their original publication.
