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

The standalone `check.py` was run with Python 3 and NumPy. Observed output:

```
FOGUEL_FULL_MODULUS_FINITE_CHECKS_OK 6858
```

The finite checks compare the positive square root of the exact block Gram matrix against the two scalar branches of singular values, verify the zero and unit block predictions, and compare Schatten-power formulas. Sizes vary from \(1\times1\) to \(6\times6\); all possible finite ranks occur, with six deterministic examples of each rank.

The analytical proof in `RESULT.md` gives the infinite-dimensional result. No finite test certifies Fredholm essential spectra, uniqueness in the literature, or publication priority. Independent audit has not been performed.
