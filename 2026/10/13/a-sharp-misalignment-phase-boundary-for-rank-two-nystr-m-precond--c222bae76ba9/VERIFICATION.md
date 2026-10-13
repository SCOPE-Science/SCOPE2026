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

# Verification

The analytic proof in `RESULT.md` derives the Nyström approximation and the specified normalized preconditioner directly, locates the three generalized eigenvalues, and reduces the comparison to the sign of a cubic with a unique zero. Its rational witness is reproduced by `verify.py` using exact fractions. Running `python verify.py` gave:

```
PASS: exact Nyström matrix, preconditioner and witness certificate
PASS: 210 rational phase-identity and convexity checks
witness preconditioned condition 1.570119803669 versus 1.5 without preconditioning
```

The tests are finite supplementary checks; the parameter-uniform assertions rely on the written algebraic proof and continuity argument. No probability magnitude, all-matrix classification, PCG iteration-count slowdown, finite-precision guarantee, or independent audit is claimed.
