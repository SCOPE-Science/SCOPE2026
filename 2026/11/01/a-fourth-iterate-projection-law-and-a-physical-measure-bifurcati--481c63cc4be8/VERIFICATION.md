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

The analytic proof derives the exact identity \(F_\mu^4=\Pi_{K_\mu}\) by the two-step scalar recurrence \(q_\mu(t)=\mu-\max(t,0)\) and the exhaustive evaluation of \(q_\mu^2\). This covers all real parameters and phase points, including branch boundaries. The classification of invariant and physical measures uses finite-order rotation and the geometry of orthogonal-projection fibers; it does not follow from a finite computational grid.

`verify.py` uses only Python's standard library (`fractions` and `itertools`). Execute `python verify.py` in the directory containing that file. The program checks exact rational identities on grids for the forcing values `-4`, `-1`, `0`, `1`, `2`, `5`, four denominators and 18 values per coordinate, plus corner orbits and sharpness witnesses. The original execution returned:

```
PASS: 31122 exact rational identities and boundary witnesses
```

The finite grid is a regression check, not an exhaustive enumeration of all real initial conditions and not a substitute for the proof. The precise set of invariant measures and their ambient-Lebesgue basins is established symbolically in `RESULT.md`. Independent mathematical audit has not been performed.
