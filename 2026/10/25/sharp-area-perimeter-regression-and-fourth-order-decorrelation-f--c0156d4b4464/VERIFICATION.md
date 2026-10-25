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

Execute `python3 verify_area_perimeter.py` in a directory containing the checker. It uses only the Python 3 standard library.

Checks actually completed successfully:

```
EXACT_FACTORIAL_INFLUENCE_MOMENTS_AND_CONSTANTS_OK
INDEPENDENT_CARTESIAN_SHOELACE_AND_GAP_GEOMETRY_OK
EXACT_DIRICHLET_MIXED_COVARIANCES_MATCH_ASYMPTOTICS_OK
TAYLOR_DIRICHLET_FINITE_N_CONVERGENCE_OK 1000 slope 0.98732681 residual 0.94637283 correlation 0.96268037
TAYLOR_DIRICHLET_FINITE_N_CONVERGENCE_OK 10000 slope 0.99873025 residual 0.99453011 correlation 0.9962052
ALL_CYCLIC_POLYGON_LINEAR_PREDICTION_CHECKS_OK
```

The checker confirms factorial constants using exact rational arithmetic, reconstructs finite polygon areas/perimeters from Cartesian vertices independently of the gap formulas, and tests convergence using eleven-degree sine truncations and high-precision numerical moments. Truncation and finite-n numerical tests are not infinite proofs. The proof of the asymptotic regression and joint limit appears in RESULT.md; independent external audit has not occurred.
