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

# Reproducibility and verification

The analytical argument in `RESULT.md` proves the all-positive-parameter statement. The `checker.py` file recomputes the model equilibrium using exact rational arithmetic, verifies the linearized balance equation and the determinant identity, and applies the explicit inverse.

Executed with Python 3: `python checker.py`.

Actual output:

```
Exact example: [(Fraction(3, 4), Fraction(1, 4), Fraction(41, 68)), (Fraction(1, 2), Fraction(1, 4), Fraction(13, 34)), (Fraction(3, 4), Fraction(1, 2), Fraction(17, 36))]
All-positive rational L-design cases: 2500
PASS: equilibrium, determinant, recovery, single-axis alias, and no finite rounding
```

No floating-point tolerances, external datasets, external packages, or network queries are used by the checker. The rational census is deliberately finite, not an exhaustion of continuous parameter ranges. The independent audit has not been performed. Practical inference from finite noisy sampling, detection error, or unequilibrated populations is not verified.
