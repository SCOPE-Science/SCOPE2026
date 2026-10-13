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

# Verification instructions and scope

Run `python verify.py` using Python 3 and its standard library. The verifier constructs small positive-rational coefficient populations, computes the exact all-mask value of the corrected scalar Gram estimator, checks strict positivity below the sorted-coefficient cutoff, zero at the cutoff, negativity above it, the variance-optimal minimum, and rational-square sharpness witnesses. Its successful execution output is:

```text
VERIFY_OK coefficient_arrays= 1364  mask_tests= 449376  positivity_threshold_tests= 5456  square_contrast_equalities= 9
```

Computational checks use `fractions.Fraction` and exhaustive binary masks only for the declared finite ranges; they are not exhaustive across all population sizes, coefficients, or sketches. The infinite-size and all-finite-repetition result requires the deterministic affine-vertex, sorted-subset, and continuous-extremum proof in `RESULT.md`. The public 2025 primary manuscript was inspected; the later 2026 preprint abstract was available but its full text was not. Independent validation and audit have not been performed.
