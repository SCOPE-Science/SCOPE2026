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
# Reproduction of finite checks

Place the embedded `verify.py` alongside this file. Run `python3 verify.py` with Python 3 and its standard library only. The checker enumerates 100 distinguished edge charts for 12 distinct complete multipartite part-size patterns, verifies monomial chart generation, enumerates all semigroup relations up to degree four against minor-swap equivalences, and verifies Jacobian rank for 28 nonzero rank-one matrix specializations at sizes 2 through 8 (plus the zero-matrix rank). An observed successful run printed:

```
OK: 100 chart presentations, minor semigroup kernels up to degree 4
OK: 28 nonzero rank-one Jacobian points for m=2..8, codimension m-1
```

The proof of the infinite presentation, singularity classification, multiplicities and local class groups is in `RESULT.md`; no finite bound on the graph sizes is part of the theorem. The calculation does not examine the scheme-theoretic Jacobian singular scheme or all potentially relevant unpublished literature. It is not an independent audit.
