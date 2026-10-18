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

# Reproducibility and scope

The proof in `RESULT.md` establishes the exact domain, the strict support-curvature formula, the nonzero cubic obstruction, and the sharp Hausdorff minimax asymptotic. For numerical diagnostics, from this package directory run:

```sh
python3 checker.py
```

Observed output from the included file: `CHECKS_OK: 25215`. The checker uses only the Python standard library, tests multiple non-Hilbert and Hilbert exponents and coupling magnitudes, and compares approximate minimax reflection defects with the predicted cubic coefficient. Its finite samples are not a proof of any all-parameter theorem.

The sharp symmetry-defect error term is an asymptotic for the dimensionless ratio of diagonal gap to nonzero coupling tending to zero at fixed exponent. No independent mathematical audit has been performed.
