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

# Arithmetic reproduction

Run `python verify.py` with Python 3.10 or newer from this extracted package. It has no third-party dependencies. The script checks every one of 24 permutations, all 16 interval vertices, 32 invariant edges, 64 oriented edge characters, 32 exact Chern-degree identities, and four exact rational localization sums. Expected outputs:

```
VERIFY_OK boolean_interval=16 edges=32 tangent_weights=64
VERIFY_OK anticanonical_degrees=0:4,2:24,4:4 nef_not_ample
VERIFY_OK anticanonical_volume=320 independent_generic_cocharacters=4
```

This verifies finite arithmetic, not the published external toric-geometric theorems. Those identifications, the toric Mori-cone criterion, and fixed-point localization are used and explained in `RESULT.md`. Independent scientific validation has not been performed.
