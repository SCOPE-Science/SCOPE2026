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

# Reproducibility checks

`verify.py` is a standalone Python 3.9+ diagnostic requiring Shapely 2.x (tested with 2.1.2). Execute:

```sh
python verify.py
```

The output from the delivered program was:

```text
VERIFY_OK geometric_cases 240 max_area_error 1.78e-15 max_perimeter_error 7.11e-15 max_coverage_error 0.00139
```

The direct polygon-union calculations use coordinate-defined polygons; angular coverage tests independently use the polygons' supporting halfplanes rather than the nearest-vertex/gap identity. The deterministic random seed and tested orders are in the source. The angular sampling discrepancy arises from finite quadrature; no error interval outside the tested configurations is claimed. Exact validity for arbitrary real rotation angles and all dimensions in the stated planar range follows from the proof in `RESULT.md`, not the finite diagnostics. The earliest source date is taken from the first arXiv version, not the subsequent journal appearance. Independent audit has not been performed.
