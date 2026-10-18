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

The proof reduces the infinite claim to integer extreme potentials of a totally unimodular incidence-inequality polytope and a sharp two-variable variance bound. The two cases of the endpoint-set size are treated explicitly and include the equality conditions.

Reproducible finite checks: `python verify_triangular_inballs.py` (Python 3, standard library only) verifies every integral admissible normalized potential for graph orders \(n=4,5,6\), counts all maximizers, and tests exact centered contact norms and rational span ranks through \(n=8\). The verifier printed:

```
n=4 N=6 tested 69 normalized integer potentials; max(N*norm2)=12; contact facets=6
n=5 N=10 tested 1133 normalized integer potentials; max(N*norm2)=36; contact facets=20
n=6 N=15 tested 34887 normalized integer potentials; max(N*norm2)=90; contact facets=20
n=4: 6 contacting normals, span rank 3, predicted center dimension 2
n=5: 20 contacting normals, span rank 4, predicted center dimension 5
n=6: 20 contacting normals, span rank 5, predicted center dimension 9
n=7: 70 contacting normals, span rank 6, predicted center dimension 14
n=8: 70 contacting normals, span rank 7, predicted center dimension 20
ALL EXACT TRIANGULAR-GRAPH TESTS PASSED
```

Finite checks cannot certify the infinite theorem by themselves. The proof supplies the missing all-dimension inequalities and the equality classification. No independent scientific audit has been performed.
