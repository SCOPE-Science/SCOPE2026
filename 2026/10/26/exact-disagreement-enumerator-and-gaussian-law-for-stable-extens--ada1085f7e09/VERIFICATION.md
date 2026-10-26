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
# Verification record

`checker.py` runs with Python 3 and no external packages. The actual command `python3 checker.py` returned:

```
FACTOR_CHECK_OK: exact 16 x 16 characteristic polynomial
ENUMERATION_OK: every pair on all cycles 3 <= n <= 16
EXTREMA_OK: Perrin diagonals and parity-sharp extremal counts
ALL_CHECKS_OK
```

The independent enumeration test uses all vertex subsets for each cycle and does not derive its answer from the transfer recursion. The determinant factor is recovered by traces and Newton identities over exact integer polynomials. These checks are finite. Infinite validity requires the local-coding bijection, determinant identity, direct extremal proof, and analytic Perron--Frobenius perturbation proved in `RESULT.md`. The displayed algebraic mean and variance constants follow from twice implicitly differentiating the dominant-root factor; they are not inferred from sample data. No independent audit has been conducted.
