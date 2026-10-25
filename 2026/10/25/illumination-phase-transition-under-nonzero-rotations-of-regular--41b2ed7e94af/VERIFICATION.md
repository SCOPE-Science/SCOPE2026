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

# Reproducible verification

Run `python verify.py` using only Python's standard library. The recorded successful execution emitted:

```text
VERIFY_OK cases=180 checked_planes=6660 vertices=6300 ordinary_directions=900
```

The script reconstructs all listed facet planes at each of 180 tuples of dimension, twist and height: integers from 3 through 32, twist/step ratios 0.03, 0.50, 0.97, and heights 0.5, 3. It validates support and exact intended vertex incidences to a floating tolerance, strict vertex-illumination tests for 2n cyclic block directions, perfect fractional coverage multiplicity, ordinary cyclic block covers, and the odd antiparallel chord obstruction.

Numerical tolerance checks are finite evidence only. The analytic proof in RESULT.md supplies the all-integer, all-height, and all-angle result; there is no external expert review or formal machine proof.
