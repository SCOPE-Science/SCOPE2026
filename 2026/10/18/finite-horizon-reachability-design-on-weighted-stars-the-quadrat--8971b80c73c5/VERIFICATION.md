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
# Reproducible verification

Run `python3 verify.py` from this directory using only the Python standard library. The program computes exact formal Gramian determinant coefficients by direct permutation expansion for eight diagonal examples in dimensions two, three and four; it compares three coefficients with the universal Hilbert/Vandermonde/trace formula. It also explicitly assembles fifteen weighted-star Laplacians and their hub-Kalman matrices, with up to five leaves, comparing exact determinants against the product of spoke weights and pairwise differences. The observed output was:

```
VERIFY_OK 39 exact coefficient/determinant identities across 23 finite test instances
```

All calculations in this program use `fractions.Fraction`. These tests do not exhaust continuous parameters, positive horizons, or arbitrary graph sizes. The general theorem is established by the analytic proof in RESULT.md; in particular, no numerical computation is offered as a replacement for the matrix factorization, the Schur/Jacobi moment calculation or the constrained-Hessian perturbation.

Independent audit has not been performed.
