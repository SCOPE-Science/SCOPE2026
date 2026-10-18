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

The `check.py` program uses NumPy and SciPy. The executed version printed:

```
PASS 321 independent generator/age/semigroup checks
```

For dimensions 1, 2, and 5, and nine distinct scale/rate combinations, the program separately obtained stationary first and mixed moments using linear generator equations and exponential-age Gaussian Wick integrals. It then computed both time-ordered covariance functions using matrix exponentials of the exact polynomial Markov generator and compared them to the proved closed forms at five distinct dimensionless lags. It checked the dimension-independent ratio, the clock-rate inversion and the normalized directional difference.

The proof in RESULT.md independently establishes the stationary moment formulas, temporal conditioning, universal ratio and global normalized maximum without relying on numerical experiments. Tests are finite and do not certify untested dimensions or an infinite range of lags by enumeration. There has been no independent external audit or experimental validation. The self-review and the scientific limits are in REVIEW.md.
