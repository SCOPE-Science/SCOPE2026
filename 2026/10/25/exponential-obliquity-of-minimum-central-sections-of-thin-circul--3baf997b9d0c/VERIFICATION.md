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

Run `python3 verify.py` with Python 3 and `mpmath` installed. The following outputs were observed from the packaged version:

```text
INDEPENDENT_INTEGRAL_AND_DERIVATIVE_IDENTITY_OK 4
INDEPENDENT_CARTESIAN_PLANE_SECTION_CHECKS_OK 9
ASYMPTOTIC_RATIO 0.4 1.01655212979 1.01736443851
ASYMPTOTIC_RATIO 0.35 1.00374976128 1.00390357407
ASYMPTOTIC_RATIO 0.3 1.00033744785 1.00034790594
ASYMPTOTIC_RATIO 0.25 1.00000495853 1.00000506498
ASYMPTOTIC_RATIO 0.2 1.00000000142 1.00000000144
ASYMPTOTIC_RATIO 0.15 1.0 1.0
ASYMPTOTIC_RATIO 0.1 1.0 1.0
ALL_BICONE_CENTRAL_SECTION_CHECKS_OK
```

The high-precision calculations test a finite number of shapes and cannot independently certify universal asymptotics or uniqueness. The analytical argument is in `RESULT.md`. Independent validation has not been performed.
