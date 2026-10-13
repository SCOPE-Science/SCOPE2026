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

The analytic proof checks the exact-line reduction, the first \(A\)-conjugacy identity, the induced gradient orthogonalities, and the strict third-direction defect. No finite experiment is used to prove the universal statement.

The packaged `verify.py` uses `fractions.Fraction` only. It reconstructs the witness with \(A=\operatorname{diag}(1,2,3)\), \(b=0\), and \(x_0=(1,1,1)^{\mathsf T}\), verifies the exact line searches and RMIL coefficients, checks \(d_1^{\mathsf T}Ad_0=0\), checks \(d_2^{\mathsf T}Ad_1=-38/4067\), and verifies that the third exact line search leaves \(\lVert g_3\rVert^2=5954786298/95440179883801>0\). A successful replay prints `VERIFY_OK`.

Limits: exact arithmetic and exact line search only; no claim is made about convergence speed under Wolfe or Armijo searches or about failure on every three-dimensional quadratic.
