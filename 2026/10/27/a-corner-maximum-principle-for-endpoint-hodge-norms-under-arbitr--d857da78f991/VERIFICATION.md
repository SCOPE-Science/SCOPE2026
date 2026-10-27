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

The exact-rational program `verify.py` independently computes canonical cut and cycle projectors of explicitly subdivided graphs using incidence matrices. It compares them with the fundamental-cycle Gram formulas, tests coordinatewise quasiconvex interpolation on a rational sample, exhaustively checks finite integer subdivision boxes, and checks the stated diamond formula. The recorded successful execution was:

```
PASS direct_projection_cases=28 midpoint_pairs=216 box_instances=2052 diamond_lengths=17
```

Run with `python verify.py` using Python 3.10 or newer. The program uses only the standard library. Finite tests do not certify all graphs or lengths; the complete proof is the rank-one update plus the fractional-convex argument in `RESULT.md`. No independent mathematical audit has been performed.
