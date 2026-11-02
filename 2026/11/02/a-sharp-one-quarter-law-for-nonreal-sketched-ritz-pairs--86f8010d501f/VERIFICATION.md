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

# Reproducible exact and supplementary checks

The proof in `RESULT.md` is analytic. The executable `verify.py` uses SymPy for algebraic exactness and Python's seeded pseudorandom generator for a supplementary angular experiment. Run `python verify.py` from the extracted package directory. The successful test returned:

```
PASS: symbolic identities, SPD determinant, 4800 exact cases, 100000 angular samples, observed rate 0.249330
```

The symbolic checks reconstruct the characteristic discriminant, the balanced-residual formula, the derivative defining the unique maximum, the sharp half-gap boundary, and the positive-definite example's exact determinant. The 4,800 rational test cases check the discriminant identity and a necessary-quadrant condition; they do not exhaust infinitely many parameter choices. The 100,000 sample directions illustrate the exact probability but do not certify it. All arbitrary-dimensional assertions use the analytic reduction and the two-by-two discriminant in `RESULT.md`. The indicated source full-text access limitation and the absence of independent validation remain unresolved.
