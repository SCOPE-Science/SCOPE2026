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
# Verification evidence

The standalone `verify.py` is supplied in this package and uses SymPy and NumPy. Execute `python verify.py` in a directory containing that file. The executed output was:

```text
exact distinct-eigenvalue counts: 31
full-matrix checks: 1331
PASS
```

Exact rational eigenspace calculations for \(2\le m\le9\) reconstruct the claimed spectrum, including the collision of the two negative eigenvalues at \(m=2\). Full-matrix checks cover \(2\le m\le12\), together with 120 independently sampled feasible transition matrices for each size. These finite computations check formulas and catch coding mistakes; they cannot prove global minimality or uniqueness over infinite parameter domains. The analytical proof in `RESULT.md` supplies those statements.

No independent audit has been performed.
