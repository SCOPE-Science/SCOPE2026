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

# Verification of the exact Radon mean-section radii

The analytic proof in `RESULT.md` is the evidence for the universal result. The embedded `verify_mean_body.py` separately tests normalization, numerical KKT maximization, random-direction inequalities, cube equality, and the three-dimensional active-set boundary. The code uses only NumPy, SciPy, and the Python standard library. Executed with `python verify_mean_body.py` in a local environment, the actual output was:

```
PASS: 500 independent constrained optimizations, 1500 random-direction/quadrature comparisons, equality and phase-boundary tests
```

The projection average is estimated using independently sampled unit normals orthogonal to a random support direction, rather than invoking the closed-form beta integral directly. The SLSQP optimizations start from balanced weights and maximize the original strict-concavity objective, not the analytic water-filling multiplier equation. The code tests finite cases only and therefore neither proves the theorem nor exhaustively checks all real inputs.

The complete proof requires no machine-generated certificate. External independent mathematical audit has not been performed. Historical literature priority remains provisional; the perpendicular-disc Minkowski sum is an established object.
