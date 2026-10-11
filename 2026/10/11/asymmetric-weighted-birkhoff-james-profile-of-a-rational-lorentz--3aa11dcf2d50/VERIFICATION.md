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

# Exact verification of the weighted Birkhoff–James profile

Execute `python3 verify_weighted_james.py` using only the Python 3 standard library. The checker represents every coordinate, facet, breakpoint, endpoint polynomial and quadratic discriminant with `Fraction`; it performs no floating-point comparisons. The expected confirmation is:

`WEIGHTED_JAMES_OCTAGON_ALL_PARAMETERS_EXACT_OK test_points= 2488 critical_polynomials= 3840 lower_families= 3`

The proof's infinite weight quantification comes from exhaustive analytic reduction to 768 affine-parameter/facet pairs and algebraic root partitioning. The checker identifies every possible change in feasibility using all polynomial roots, then checks critical points and one representative point in each interval. The four paths follow from supporting functionals of the explicitly given octagon. The three witnesses are checked at each endpoint of the affine lower bound, hence for every weight. The final reflection difference is a piecewise-affine calculation on the explicitly listed six breakpoints.

Scientific limits: the checker does not investigate higher-dimensional norms or independently establish that no published equivalent formula exists. The full first version of the motivating primary preprint was available and its examples, statements, applications and references were compared; it does not give the octagonal result. No independent audit has been performed.
