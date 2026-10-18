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

# Verification notes

The complete proof is in `RESULT.md`. Its independently checkable steps are (1) the coprime intermediate function-field degrees, (2) the derivative roots and critical-value parities, (3) the explicit Frobenius transformation of tangent slopes, and (4) the normalization point-count correction at each rational node. The equation is affine and the polynomial characteristic assumptions are explicit.

Run `python3 verify.py`; the recorded output is:

```
PASS: 84 prime-field tests and 8 quadratic-field tests
Example p=5, n=3, m=2: 6 and F25: 24
```

The checks use exact modular arithmetic; the quadratic extensions use irreducible quadratic binomials. Finite experiments are corroboration, not a proof for all q or all extension degrees. No independent audit has been performed.
