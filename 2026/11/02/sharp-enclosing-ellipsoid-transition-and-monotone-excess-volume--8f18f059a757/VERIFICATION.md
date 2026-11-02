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

Run `python3 verify_cap_lowner.py` with SymPy and mpmath available. The executable tests the exact containment factorization at a rational sample of dimensions and truncation heights, the affine regular-simplex frame identities, numerical strict monotonicity and thin-cap ratios for several dimensions, independent planar and spatial hemisphere benchmarks, and the dimension-varying normal boundary layer through regularized beta integrals. In the present run it returned `EXACT_CONTAINMENT_AND_SIMPLEX_FRAME_PASSED`, `SHARP_RATIO_MONOTONICITY_AND_THIN_CAP_LIMIT_PASSED`, `HEMISPHERE_BENCHMARKS_PASSED`, `GAUSSIAN_BOUNDARY_LAYER_PASSED`, and `ALL_CHECKS_PASSED`.

These finite computations do **not** establish parameter-uniform inequalities or uniqueness. Their mathematical justification is the explicit affine-simplex trace/determinant certificate, the exact factorization of the candidate containment defect, the weighted-integral derivative bound and standard endpoint/central-limit arguments detailed in RESULT.md. No independent audit has been performed.
