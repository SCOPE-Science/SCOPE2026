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

# Verification of the complete-bipartite graphical-zonotope theorem

The standalone script `verify_k2m.py` enumerates **all** edge-sign cones via weak orderings of the \(m+2\) vertices of \(K_{2,m}\), deduplicates sign vectors, computes equality-block contractions and exact cover relations, and tests which singular cones have no singular proper face. It is independent of any symbolic toric package and uses Python 3 standard-library integer operations only.

Run with `python verify_k2m.py` from the directory containing this file. Observed exact output includes:

```
m= 2  minimal_singular_cones= {3: 6} checked_total= 51
m= 3  minimal_singular_cones= {3: 12, 4: 8} checked_total= 261
m= 4  minimal_singular_cones= {3: 48, 5: 16} checked_total= 1299
m= 5  minimal_singular_cones= {3: 160, 6: 32} checked_total= 6429
VERIFY_OK
```

The total includes the zero cone. These finite computations do **not** prove the all-parameter statement; the proof in `RESULT.md` handles arbitrary \(m\ge3\). In particular the integral tree-incidence argument proves unimodularity, and the explicit dual semigroup decompositions prove the conifold and rank-one determinantal chart descriptions. There is no assertion of an independent review or external validation.
