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

# Reproducibility and mathematical limits

Run the standalone `check_polyhedral_surface_euclidean.py` with Python, NumPy and SciPy. It independently quadratures the original angled facet-pair integral at four angles, quadratures same-face and adjacent-face unit-cube contributions at three radii, and directly samples cube face pairs using 1,048,576 deterministic Sobol points. The numerical tolerance of the sample comparisons is 0.002; it is not a certified confidence interval.

Expected checkpoint lines from execution:

```text
DIRECT_TWO_FACET_WEDGE_QUADRATURE_OK alpha=0.75000000 value=2.3390616791
DIRECT_TWO_FACET_WEDGE_QUADRATURE_OK alpha=1.23095942 value=1.3510217183
DIRECT_TWO_FACET_WEDGE_QUADRATURE_OK alpha=1.57079633 value=1.0471975512
DIRECT_TWO_FACET_WEDGE_QUADRATURE_OK alpha=2.40000000 value=0.7319349398
INDEPENDENT_CUBE_FACE_PAIR_INTEGRALS_OK 0.2 P=0.0226879034
INDEPENDENT_CUBE_FACE_PAIR_INTEGRALS_OK 0.45 P=0.1218277796
INDEPENDENT_CUBE_FACE_PAIR_INTEGRALS_OK 0.8 P=0.3918913957
DIRECT_FACE_SAMPLING_CUBE_CDF_OK 0.35 got=0.07240486 wanted=0.07233958
DIRECT_FACE_SAMPLING_CUBE_CDF_OK 0.6 got=0.22020626 wanted=0.22016281
DIRECT_FACE_SAMPLING_CUBE_CDF_OK 0.8 got=0.39179611 wanted=0.39189140
QUADRATIC_HINGE_DEFECT_SCALING_OK
ALL_POLYHEDRAL_SURFACE_EUCLIDEAN_CHECKS_OK
```

The infinite assertion that every convex polyhedron has an exactly quartic small-radius law rests on the facetwise coarea and polyhedral-cell proof, **not** the numerical tests. The cube is a known special case, not a novelty argument. No independent mathematical audit has been performed. Scientific limits and bibliographic comparison are stated in RESULT.md and REVIEW.md.
