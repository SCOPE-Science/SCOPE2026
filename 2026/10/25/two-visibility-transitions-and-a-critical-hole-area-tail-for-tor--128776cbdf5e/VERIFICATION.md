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
# Reproducibility and limits

Executed: `python verify_torus_shadow.py` from the same embedded package.

```text
THREE_SHADOW_PHASES_AND_3HALVES_HOLE_EXTINCTION_OK 0.25
THREE_SHADOW_PHASES_AND_3HALVES_HOLE_EXTINCTION_OK 0.4
THREE_SHADOW_PHASES_AND_3HALVES_HOLE_EXTINCTION_OK 0.65
HAAR_PHASE_PROBABILITIES_AND_SHARP_QUARTER_MAXIMUM_OK
TORUS_SHADOW_REPRODUCTION_CHECKS_OK
```

The independent numerical construction uses NumPy and Shapely to approximate planar ellipses with 12,000-vertex polygons and compute inner and outer metric offsets. It checks thresholds on both sides and finite-epsilon proximity to the derived leading constants. Approximate polygon buffers do not prove exact geometry, the universal asymptotic, or historical priority. Those rest on the analytical argument and source comparisons.
