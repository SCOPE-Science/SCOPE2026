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

# Reproducible mathematical checks

Run `python verify.py` in a Python 3 environment with SymPy, NumPy and SciPy. The executed checker returned `PASS: 2008 assertions; exact crossover identity, explicit witness, independent direct-sketch checks and 32/27 limit.` Its symbolic assertions cover the closed-form trace and determinant comparison, the transformed cubic, endpoint signs, the exact Nyström sketch and preconditioner, and the generalized-eigenvalue polynomial. It independently constructs 500 real Gaussian sketch matrices and compares direct generalized eigenvalues with the closed-form formula. It checks the limiting relative ratio analytically.

The manuscript's universal proof is algebraic. The random trials alone cannot certify uniqueness, global domain coverage, or probabilistic positivity; those assertions follow from the stated projector reduction, polynomial sign argument, continuity, and full-support Gaussian density. No finite-precision performance claim and no independent scientific audit is made.
