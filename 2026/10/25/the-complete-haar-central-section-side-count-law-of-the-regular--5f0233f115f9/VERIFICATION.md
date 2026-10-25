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

`python verify.py` was executed from the packaged source with NumPy and SciPy. The actual output was:

```text
EXACT_SPHERICAL_CHAMBER_PROBABILITIES_OK {4: 0.1510526932733458, 6: 0.5002272882524017, 8: 0.28139735629611207, 10: 0.06732266217814019}
INDEPENDENT_24_VERTEX_36_EDGE_14_FACET_CONSTRUCTION_OK 4000
ANALYTIC_SOLID_ANGLES_AGREE_WITH_INDEPENDENT_GNOMONIC_QUADRATURE_OK
INDEPENDENT_EDGE_CROSSING_MEAN_IDENTITY_OK 6.529979974758095
INDEPENDENT_HAAR_RANDOM_3D_EDGE_COUNT_DISTRIBUTIONS_OK 450000 {4: 0.15224444444444443, 6: 0.50002, 8: 0.28058666666666665, 10: 0.06714888888888888}
ALL_REGULAR_TRUNCATED_CUBE_CENTRAL_SECTION_CHECKS_OK
```

Finite sampling is corroborative only. The mathematical proof depends on exact face incidence, the six-cell planar decomposition and the spherical Jacobian. No external expert audit has been performed.
