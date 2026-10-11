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

# Verification

Run `python verification/check.py` with Python 3 and SymPy. The script uses exact rational coefficients, verifies the midpoint/Cayley sextic identity, isolates every real sextic root with Sturm root counts, rules out the excluded unit-circle pole, proves the single admissible positive branch, and checks the strict inequalities for the two-step multiplier determinant and discriminant. It does not depend on a numerical orbit-finding tolerance.

Successful output:

```
PASS: sextic identity, exact two-real-root count, unique positive branch, conjugate repelling multipliers.
```

The exact computation certifies the displayed algebraic root counts and inequalities but is not an independent proof-assistant certification or external audit. The mathematical derivation and quantified scope are given in `RESULT.md`. The numerical coordinates are descriptive approximations, not an additional source of existence or uniqueness.
