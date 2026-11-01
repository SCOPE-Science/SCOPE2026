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

# Verification of the weighted metric-star projection formula

`verify_star.py` uses exact fractions. It constructs a symmetric nodal Gram matrix, inverts it by an independent Gauss–Jordan algorithm, evaluates projection kernels from the inverse basis representation at distinct graph points, and integrates absolute affine kernels using exact zero-crossing formulas. It compares with the closed-form center and leaf values and checks strict endpoint domination for interior samples.

Recorded command: `python verify_star.py`

Recorded output:
```
PASS: 27416 exact-rational assertions over 382 weighted metric stars
equilateral d=1..7: ['5/3', '17/9', '2', '31/15', '19/9', '15/7', '13/6']
```

These finite computations support the symbolic derivation; they do not enumerate infinitely many mass vectors or degrees. The formulas for the full stated scope are established by the Gram inversion, affine kernel and convexity argument in `RESULT.md`. No independent human or external mathematical audit was performed.
