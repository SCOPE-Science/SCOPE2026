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

# Mathematical verification

Execute `python3 check_counts.py` in the same directory as this file. It uses only Python standard-library integer operations and enumerates all normalized points in the hyperplane and, independently, coordinate multisets weighted by permutation orbits. The two counts coincide.

```text
F_5: points=41, charts=[23, 12, 5, 1], sorted_affine_orbits=10, weighted_nonzero=164
F_25: points=901, charts=[803, 72, 25, 1], sorted_affine_orbits=308, weighted_nonzero=21624
Y: F_5=96, F_25=1176, traces=70,550; eigenvalues +5 x18, -5 x4
CHECK_OK
```

The finite computations prove the two stated finite counts because the code exhaustively enumerates all representatives and implements exact finite-field arithmetic. They are not substituted for the geometric analysis of singularities or the Weil theorem; those are detailed separately in `RESULT.md`. No external audit or external certification is represented here.
