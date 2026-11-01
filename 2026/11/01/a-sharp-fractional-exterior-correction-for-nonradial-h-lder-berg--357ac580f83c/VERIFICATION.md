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

The proof in RESULT.md establishes all infinite-degree statements. The standalone `verify.py`, with `mpmath>=1.3` from `requirements.txt`, checks the Beta integral moments, finite tridiagonal Gram entries, monic polynomial recursions, orthogonality up to degree 13, and asymptotic coefficients at degree 1500. Run `python verify.py` in the directory containing these files.

Observed output includes:

```
CHECK_OK: Gram orthogonality, beta moments, monic recurrence, fractional asymptotics
n=1500 first-coefficient ratio: (0.99901400708 - 0.0012381758495j)
n=1500 normalization-response ratio: 0.99869569251
```

The numerical checks corroborate finite specializations, not uniqueness, novelty, the all-degree theorem, or the infinite-dimensional estimates. Full source inspection and independent external validation are not claimed. The analytical proof verifies the limit, uniform quantifiers and Hölder boundary regularity.
