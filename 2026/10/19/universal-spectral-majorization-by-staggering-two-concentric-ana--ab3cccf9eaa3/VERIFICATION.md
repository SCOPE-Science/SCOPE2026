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

The theorem is proved analytically in `RESULT.md`, using Fourier block diagonalization, a self-contained algebraic recurrence proving simple negative numerator roots, and a two-entry-to-full-spectrum majorization argument. No formal proof certificate or external independent audit is claimed.

Run `python checker.py` with Python 3, `numpy` and `sympy`. The checker was actually executed and printed:

```
PASS root_cases= 80 all_polynomial_cases= 243
PASS independent_kernel_spectrum_cases= 42
```

The 80 nonconstant polynomial root counts used exact rational Sturm computations; 243 numerator-polynomial coefficient tests were exact. For seven choices of \((n,\alpha,r,s)\), and six offsets each, floating-point diagonalizations of directly assembled \(2n\)-by-\(2n\) Gram matrices agreed with their independently calculated Fourier-block spectra. They also satisfied the predicted majorization inequalities and endpoint determinant/conditioning order within numerical tolerances.

The test set is finite, with floating-point checks where transcendental values occur. These checks are not used to infer the theorem for untested parameters. The theorem excludes noninteger kernel exponent, unstructured angles, coincident radii, and boundary nodes. No independent proof audit has been performed.
