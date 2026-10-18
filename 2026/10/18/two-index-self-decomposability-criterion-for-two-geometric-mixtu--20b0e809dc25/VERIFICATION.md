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

## Reproducibility

Run `python3 checker.py` with the standard Python library. The checker uses `fractions.Fraction` for probability and defect identities and seeded selection of rational triples for reproducibility; the two candidate indices use ordinary floating-point logarithms as a supplementary test. Successful output was:

```
N 90 first_failure 16 at_third True
N 180 first_failure 32 at_third True
N 360 first_failure 64 at_third True
N 720 first_failure 129 at_third True
PASS exact rational cases 375 each with 99 levy checks and 180 full defect checks; delayed families 4
```

All \(375\) cases also check \(16\) exact generating-function coefficients, positivity of the jump terms and the canonical defect identity. These finite checks do not replace the real-parameter analytical proof; positivity for infinitely many jump indices and arbitrarily late failure rely on the formula and limit argument. The standalone checker uses no data files or external services. Formal independent verification has not been performed.
