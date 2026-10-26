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

# Computational verification

Run `python verify.py` in the package directory after installing `sympy>=1.11,<2` from `requirements.txt`. The checker performs four exact symbolic adjacent-class difference comparisons (positivity after shifting the size variable by five), enumerates all existing-edge pairs for triangular graphs on underlying sets of sizes 5 through 9 and verifies the five integer invariant classes and all closed-form class counts. Separately, for sizes 5 through 7, it computes the Kirchhoff index via exact rational inverses of grounded Laplacian matrices before and after deletion of one representative of each class, providing 15 direct matrix checks.

Recorded execution result:

```
matrix_n 5 classes 5 pairs 435
matrix_n 6 classes 5 pairs 1770
matrix_n 7 classes 5 pairs 5460
orbit_n 8 classes 5 pairs 14028
orbit_n 9 classes 5 pairs 31626
VERIFY_OK symbolic_differences=4 orbit_classifications= 25  exact_matrix_comparisons=15
```

These finite checks neither exhaust all integers nor supply a replacement for the spectral-projector proof. The formal universality comes from the exact symbolic formulas, denominator bounds and strict factor-sign arguments in `RESULT.md`. Independent audit has not been performed.
