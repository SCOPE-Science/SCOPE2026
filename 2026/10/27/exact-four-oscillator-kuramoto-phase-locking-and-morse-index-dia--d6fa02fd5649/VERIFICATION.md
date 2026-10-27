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

The included `verify.py` was executed against the included source in a Python 3 environment with NumPy, SciPy, and SymPy. It printed `VERIFY_OK`, reproduced the algebraic fold discriminant, and gave equilibrium counts 0, 2, 4, 4, 8, 8 for six couplings. All sampled roots satisfy the four original vector-field equations to numerical tolerance, and the sampled Hessian eigenvalues match the analytically derived unstable indices. The theorem's exhaustive classification is the four-sign-family argument and exact monotonicity proof in `RESULT.md`; the finite test is a reproducibility check and is not offered as an independent proof. No independent audit has been performed.
