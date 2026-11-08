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

# Reproducibility and limits

Run `python verify/check.py` after installing the packages in `verify/requirements.txt`. This is the code actually run against the embedded source:

```
COMBINATORIAL_EDGE_CHECK_OK n=4..10
FINITE_CROFTON_CHECK_OK n=4 hits=178961 max_abs_error=0.00269
FINITE_CROFTON_CHECK_OK n=5 hits=165526 max_abs_error=0.00171
FINITE_CROFTON_CHECK_OK n=8 hits=143336 max_abs_error=0.00207
FOUR_VERTEX_SIMPLEX_REFERENCE_OK p_quadrilateral=0.288535543072
ASYMPTOTIC_DIAGNOSTIC n=200 x=0.5 finite_CDF=0.468894 limit_CDF=0.292893
ASYMPTOTIC_DIAGNOSTIC n=800 x=0.5 finite_CDF=0.432308 limit_CDF=0.292893
ASYMPTOTIC_DIAGNOSTIC n=3200 x=0.5 finite_CDF=0.408525 limit_CDF=0.292893
GAUSSIAN_SPACING_SIMPLEX_CHECK_OK
```

The finite diagnostics are not expected to match the large-dimensional law closely at moderate \(n\); Gaussian extrema have logarithmic convergence. Exact identities and the limit follow from the analytical proof in `RESULT.md`. The checker deliberately uses a fixed, enclosing offset interval followed by intersection conditioning, rather than uniform offsets separately for each direction; only the former implements the invariant Crofton probability measure. The verifier does not certify historical priority or independent correctness.
