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

The proof was checked algebraically at the level of the voltage-difference equations, determinant recurrence, tridiagonal inverse, and the conversion \(2c=(1-\alpha)^2/\alpha\). The \(n=1\) case was checked separately.

`verify_ladder_kernel.py` provides a supplementary exact finite replay. For every \(1\le n\le5\) and each \(c\in\{1,2,3/2\}\), it enumerates all spanning trees, retains exact rational weights, and checks every nonempty rung subset against the corresponding principal determinant of \(2cB_n^{-1}\). It then checks every transfer-current entry against the closed \(\alpha\)-formula. The replay reports `VERIFY_OK`.

The exhaustive replay is finite evidence only; the all-\(n\), all-\(c>0\) statement rests on the exact recurrence and transfer-current proof in `RESULT.md`.

Literature checks found the general transfer-current theorem, the finite weighted ladder tree count, the classical unweighted endpoint marginal, and the infinite stationary ladder kernel. No inspected source stated the displayed finite-volume matrix. This is not an independent audit.
