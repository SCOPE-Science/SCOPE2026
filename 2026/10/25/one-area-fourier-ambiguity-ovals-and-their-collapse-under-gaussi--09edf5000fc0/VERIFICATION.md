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

The mathematical claim and proof are given in `RESULT.md`. This record documents reproducible checks, not an independent audit.

The companion program `checker.py` uses Python with NumPy and SciPy (`requirements.txt`). Run from a directory containing these files with `python checker.py`. It evaluates the underlying Gaussian integral as independent numerical quadratures for real and imaginary parts, then compares it with the exact four-term formula. It also evaluates the enclosed area of the balanced closed zero curve, samples the exact imbalanced isolated zeros by direct quadrature and verifies their nonzero oppositely signed Jacobians, and samples several nearby nonzeros.

Observed successful output:

```
independent_gaussian_integrals 8 max_abs_diff 1.043e-15
balanced_loop_areas 7 max_error_from_one 3.331e-15
imbalanced_isolated_zeros 24 max_abs_residual 1.567e-15
neighbor_nonzero_cases 3
CHECKS PASSED
```

The checker was actually executed, and its standard output was compared byte-for-byte with `checker_output.txt`. The finite checks cannot prove completeness of the infinitely many zero components, global nonvanishing away from them, strict convexity, exact area for all parameters, or winding-index classification. Those facts follow from the exact Gaussian identity, elementary trigonometric exhaustion, nonvanishing Jacobian, and analytic differentiation of the area integral in the proof.

An independent mathematical audit has not been performed. The 2009 discussion of symmetry-breaking cat-state blind spots uses a near-origin emphasis; the reported remote exact zeros have been directly verified for representative parameters, but the literature-priority interpretation is a residual limitation.
