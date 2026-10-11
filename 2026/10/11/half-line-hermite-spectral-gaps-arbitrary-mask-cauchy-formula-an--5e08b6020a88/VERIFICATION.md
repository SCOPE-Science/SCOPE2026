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

# Verification of the half-line Hermite concentration theorem

Run `python verify.py` with NumPy, SciPy, and mpmath available. The checker computes positive-half-line scalar products of normalized Hermite functions independently by quadrature; compares them with the boundary-Wronskian entries; enumerates 2,036 nonempty subsets of consecutive initial Hermite levels; checks spectral symmetry and exact midpoint multiplicities up to floating precision; compares noncentral products with separately assembled Cauchy–Binet maximal-minor sums; tests the gamma product by independently formed matrix determinants through size ten; and numerically checks the Barnes constant in a ten-thousand-factor product.

Expected checked output: `VERIFY_OK masks=2036 max_gram_err=4.441e-16 max_gap_err=3.220e-15 exact_barnes_cases=10 asymptotic_ratio=0.645002448 target=0.645002449`.

The analytic proof, not the computation, establishes the statements for all finite masks and all low-pass dimensions. In particular, finite numerical tests do not establish rank in arbitrary dimension, exhaustive literary originality, or asymptotic convergence. All nonstandard analytic steps required for the statement are given in `RESULT.md`, including normalization and limiting constant.
