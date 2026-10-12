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
# Verification of the matching-price frontier

`python3 checker.py` (standard library, Python >=3.9) checks the theorem's finite-dimensional spectral and optimality calculations by exact rational matrix inversion, comparing the calculated Kirchhoff index against the graph Laplacian plus its nullspace projector. It tests both price regimes, threshold decisions, budget identities and finitely many nonsymmetric feasible allocations; it exercises sample critical-window values separately.

Observed run from this file set:

```
VERIFY_OK 140 exact-rational matrix-inverse/spectrum/budget identities; 75 boundary-optimality comparisons; 23 threshold/window checks; 216 exact nonsymmetric feasible competitors
Finite tests do not prove the theorem or its asymptotic limits.
```

The analytical proof in `RESULT.md` is required for the statements for all integers n>=3 and real prices t>0; finite experiments and numerical thresholds cannot replace it. Originality comparisons against published sources remain incomplete in less-accessible historical literature. Independent audit: not performed.
