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

The analytic proof uses the normalized Laurent monomial basis, exact shift-weight differences, a two-root collision identity, and an exact monotonicity argument. The following supplementary checks were executed from the packaged standalone program:

```
python3 check_annulus.py
PASS: 67264 exact rational checks and tail comparisons
```

The checks use Python's rational `fractions.Fraction` for eigenvalues, reflection pairings, sharp extremal parameters, and periodic index reparametrization. The trace tail comparison uses numerical conversion only for a finite, explicitly bounded truncation; trace-class membership and the infinite telescoping trace are proved symbolically in `RESULT.md`. A finite experiment is not a proof of general parameter claims. No independent audit or validation has been performed.
