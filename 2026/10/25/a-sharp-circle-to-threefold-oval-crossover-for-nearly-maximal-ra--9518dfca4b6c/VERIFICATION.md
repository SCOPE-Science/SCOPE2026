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

# Computational checks and verification limits

The complete analytic argument is in `RESULT.md`. The supplied `verify_trilobe.py` is a standalone companion sanity-check program requiring Python 3, NumPy and SciPy. It computes the area of triangles directly from their three Cartesian vertices, derives numerical second derivatives independently from the closed Hessian, and uses deterministic low-discrepancy integration to compare finite rare-event probabilities with each leading asymptotic formula.

Actual observed output:

```text
HESSIAN_SPECTRAL_IDENTITY_OK 0.01 [0.03936094 0.7019353  0.70193534]
FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK 0.01 0.001 1.00414 68586
FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK 0.01 0.0002 1.00173 68586
HESSIAN_SPECTRAL_IDENTITY_OK 0.05 [0.20459854 0.92069318 0.92069326]
FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK 0.05 0.001 1.00218 68586
FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK 0.05 0.0002 1.00131 68586
HESSIAN_SPECTRAL_IDENTITY_OK 0.09 [0.382307   1.15400047 1.15400075]
FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK 0.09 0.001 1.0021 68586
FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK 0.09 0.0002 1.00131 68586
JOINT_SMALL_SHAPE_CROSSOVER_OK 0 1.00012 0.00021221
JOINT_SMALL_SHAPE_CROSSOVER_OK 0.25 0.99993 0.00015915
JOINT_SMALL_SHAPE_CROSSOVER_OK 0.5 0.99968 0.0001061
JOINT_SMALL_SHAPE_CROSSOVER_OK 0.75 0.99946 8.003e-05
JOINT_SMALL_SHAPE_CROSSOVER_OK 2.0 0.99832 4.626e-05
JOINT_SMALL_SHAPE_CROSSOVER_OK 5.0 0.99529 2.877e-05
CUSP_PROFILE_COEFFICIENT_OK
CRITICAL_PROFILE_AND_MATCHED_COEFFICIENT_OK
ALL_TRILOBE_GEOMETRY_CHECKS_OK
```

The finite experiments do not prove the global extremum, the infinity-limit probability coefficient, a uniform convergence rate, or originality. Those require the stated geometric and analytic proof and comparison with the primary literature. No independent audit or external certification is asserted.
