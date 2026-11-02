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

# Reproduction and limits

Run `python3 verify.py` in this directory (Python 3, standard library only). Supplementary checker output:

```
PASS: 1540 exact-rational geometries, 500 exact inverse tests
PASS: sharp near-extremizers for every row count 3..12
PASS: three-row near-extremizer and unique largest-volume pair
```

The program checks the exact rational parametrization of unit circle vectors, all pair determinants, a doubled-angle chord identity, the strict universal bound, and a family approaching each finite-row supremum. The full proof for every finite row count follows from the projectors and parallelogram identity in RESULT.md; finite checks alone are not the proof of the universal result. All statements concern ideal exact arithmetic and the specified population or initialized-online normalization. There has been no independent mathematical audit.
