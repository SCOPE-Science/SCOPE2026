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

The exact symbolic and rational-arithmetic checks are contained in `verify.py` and require Python 3 and SymPy (`requirements.txt`). Executing `python verify.py` on the included source produced:

```
VERIFY_OK symbolic_general_n_s=PASS exact_enumerations=270
```

The symbolic test derives the coefficients for the four conditional moments, compares them against the proposed energy weights, and checks that the drift has **exactly** the claimed polynomial coefficient of the current iterate's square with no hidden contributions from saved-gradient moments. It also verifies a sufficient positivity factorization, the scalar moment transfer determinant, and identities used for the sample-count monotonicity argument. A logically separate branch samples every possible component update for 270 configurations using Python `fractions.Fraction`, providing exact-rational consistency tests for \(n=2,3,4,5,7\).

These are executable identity checks, not a replacement for the mathematical proof. Uniform control of all \(n\), positive definiteness for every \(s>0\), the expected-energy telescoping argument, the boundary obstruction, and SPD matrix extension are proved in `RESULT.md`. No independently executed audit is represented.
