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

# Verification of the local Crofton tomography theorem

The scientific argument appears in `RESULT.md`. It uses Cauchy's perimeter formula for invariant random lines, triangle-hit inclusion–exclusion, Euclidean angle reconstruction, and a supporting-halfplane argument for the feasibility converse. Those analytic steps, not finite experiments, establish the all-polygons theorem.

`verify.py` is a standalone Python-standard-library checker. It constructs 21 nonregular convex polygons of sizes 3, 4, 5, 6, 7, 10, and 13; for every side it integrates the length of its projected offset interval and the overlap of adjacent offset intervals by numerical angular quadrature. It compares these independently computed Crofton probabilities with the algebraic length formula. It reconstructs all normalized pairwise vertex distances, verifies polygon closure, checks five regular/equilateral configurations, and checks that a perturbation satisfying local triangle inequalities can violate global closure.

Executed successfully against the actual bundled checker:

```text
ADJACENT_CROFTON_TOMOGRAPHY_OK polygon_cases=21 regular_cases=5 exact_distance_and_quadrature_checks=1162
```

To reproduce, run `python verify.py` with Python 3 in a directory containing the checker. No external dependencies are needed. Numerical quadrature is neither an exhaustive mathematical certificate nor a substitute for the theorem's proof. No independent audit has been performed.
