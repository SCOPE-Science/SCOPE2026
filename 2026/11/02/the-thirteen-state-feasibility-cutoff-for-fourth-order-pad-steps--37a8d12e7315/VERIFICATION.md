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

Run `python3 verify_gauss_birth.py` with Python 3.10 or newer. It uses only the standard library (`fractions` and `math`). The recorded run output was:

```
VERIFY_OK 27584 exact assertions
```

The verifier builds the exact finite generator, forms the Padé numerator and denominator matrices, solves an exact-rational linear matrix equation by Gaussian elimination, and compares every entry with a separately coded generating-function recurrence. Each tested row sums exactly to one. It evaluates all lengths from two through eighteen, a grid of twelve rational step sizes, and explicit nearest-neighbor and diagonal formulas. It separately checks the predicted nonnegative-step set on the grid.

The full all-integer proof and irrational boundary points rely on the sine-generating-function derivation in `RESULT.md`, not on exhaustive computation, floating-point tolerances, or external certification. No independent mathematical audit has been performed.
