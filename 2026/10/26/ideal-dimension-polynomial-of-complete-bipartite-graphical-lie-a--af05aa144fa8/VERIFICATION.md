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

Run `python3 verify.py` with Python 3's standard library. It computes the uniform formula and separately generates every row-reduced subspace of the underlying vector space, then tests closure under brackets with the ambient noncentral basis. This independently checks the finite cases (not the all-parameter proof):

```
PASS a=1 b=1 q=2: [1, 1, 3, 1], checked_subspaces=16
PASS a=1 b=1 q=3: [1, 1, 4, 1], checked_subspaces=28
PASS a=1 b=2 q=2: [1, 3, 7, 7, 7, 1], checked_subspaces=374
PASS a=1 b=2 q=3: [1, 4, 13, 13, 13, 1], checked_subspaces=2664
PASS a=1 b=3 q=2: [1, 7, 35, 43, 43, 35, 15, 1], checked_subspaces=29212
PASS a=2 b=2 q=2: [1, 15, 35, 39, 55, 51, 35, 15, 1], checked_subspaces=417199
ALL_SMALL_CASES_PASS
```

The all-fields, all-sizes proof does not rely on experimental extrapolation. It follows from the unique ideal-to-\((W,D,f)\) classification, tensor commutator dimension, and Gaussian/Goursat enumeration in `RESULT.md`. The code tests prime fields of sizes two and three; the mathematical proof covers all prime powers. The counting statement does not claim a new p-adic ideal-zeta formula.
