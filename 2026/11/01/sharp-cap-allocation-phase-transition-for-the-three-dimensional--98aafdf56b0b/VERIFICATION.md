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

The mathematical proof is in `RESULT.md`. `verify_double_caps.py` is a standalone finite exact-arithmetic cross-check.

The program was run with Python 3 and returned:

```
VERIFY_OK exact difference-body polytope reconstruction: 11 independent instances; 66 monotonicity/identity instances
```

The 11 independent convex-hull checks use exact rational vertex coordinates, explicit integer facet-side tests, exact planar convex-hull triangulations, and exact determinant volumes. They verify the analytic mixed-volume formula by the *different* identity \(\operatorname{vol}_3(K-K)=2\operatorname{vol}_3(K)+6V_3(K,K,-K)\). The 66 additional rational-grid instances check the exact factorization and derivative bound. These tests do not establish the universal real-parameter assertions; those follow from the explicit analytic proof and inequalities.

The program requires only the Python 3 standard library. No proof assistant or third-party mathematical certification is claimed. Historical-priority verification is not complete; the earlier general anti-blocking projection identity is acknowledged.
