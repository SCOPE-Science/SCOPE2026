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

# Reproducibility and actual checks

The Python standard scientific dependencies `numpy` and `scipy` are needed to run `python verify_mec_tail.py` from the package directory. The checker completed successfully and emitted:

```
INDEPENDENT_SIX_BY_SIX_CHANGE_OF_VARIABLES_JACOBIAN_OK
EXACT_ACUTE_ARC_ANGULAR_INTEGRAL_OK
EXACT_QUADRATURE 0.1 0.006766098257 0.01115887029
EXACT_QUADRATURE 0.03 0.000267687701 0.000584091805
EXACT_QUADRATURE 0.01 1.2227975e-05 3.8098248e-05
ACUTE_LOG_TAIL_AND_TWO_POINT_ENDPOINT_CONSTANTS_OK
INDEPENDENT_UNIFORM_TRIANGLE_SUPPORT_COUNT_SIMULATION_OK 1200000
ALL_MINIMUM_ENCLOSING_DISK_UPPER_TAIL_CHECKS_OK
```

The six-by-six Jacobian is compared with independent finite-dimensional determinant values, the angle integral is evaluated by independent nested adaptive quadrature, and a direct random-point sampler categorizes acute and obtuse sample triangles to test the finite-radius prediction. Small-deficit numerical quadrature converges slowly because the three-support asymptotic contains an additional \(O(\varepsilon^3)\) term. The infinite asymptotic statements are proved analytically in `RESULT.md`; finite numerical checks are not a substitute for proof. No independent audit or external validation was performed.
