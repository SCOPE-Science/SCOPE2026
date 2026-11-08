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

# Reproducible checks

Run `python verify_double_star_projection.py` after installing the dependency in `requirements.txt`. The script symbolically expands the exact leaf/hub difference and verifies that it equals the supplied polynomial with 21 positive coefficient terms. It checks the rational equality for the \(7/3\) crossing and the full derivative identity. It then independently constructs the mass matrix from the length-scaled edge Gram blocks, computes the inverse in exact rational arithmetic, and integrates all signed affine kernels at every vertex for 35 parameter pairs.

Observed successful output:

```text
SYMBOLIC_LEAF_DOMINANCE_COEFFICIENT_CERTIFICATE_OK 21
SYMBOLIC_SEVEN_THIRDS_CROSSOVER_IDENTITY_OK
SYMBOLIC_DERIVATIVE_IDENTITY_AND_DEGREE_SIGN_PATTERN_OK 199
INDEPENDENT_EXACT_GRAM_INVERSION_AND_EDGE_KERNELS_OK 35
ALL_SYMMETRIC_DOUBLE_STAR_PROJECTION_CHECKS_OK
```

The exact matrix check covers the seven degrees \(2,3,4,5,7,9,10\) and five positive rational lengths \(1/20,2/5,1,3,17/2\). The 199 degree sign checks are finite corroborations; the all-degree coefficient-sign reasoning is proved in `RESULT.md`. No computational approximation substitutes for the analytic uniqueness proof or the stated limit calculations. The source code is standalone within this package; no output logs, separate runs, private sources or network resources are dependencies.
