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

The source splitting formula was checked directly in the full preprint. On the region where the source cutoff equals one,
\[
E(\tau,\phi)
=
\Delta(\tau)+(q(\tau)-\Delta(\tau))\psi(\phi)
=
\psi(\phi)q(\tau)+(1-\psi(\phi))\Delta(\tau).
\]
Under \(q\ge0\), \(\psi\ge1\), \(\Delta\le0\), and \(q^{-1}(0)\subset\{\Delta<0\}\), this is zero exactly when \(q=0\) and \(\psi=1\). The source's positivity argument outside the nonpositive-splitting region then leaves no additional zeros.

For a relative deletion schedule \((\rho_n)\), the stage-\(N\) surviving length was recomputed as
\[
L\prod_{n=1}^N(1-\rho_n).
\]
Taking the decreasing intersection gives the infinite product. The product is positive exactly when
\[
\sum_{n\ge1}-\log(1-\rho_n)<\infty.
\]
Fubini gives the two-coordinate area formula.

For constant relative deletion \(\rho\), the similarity ratio is \((1-\rho)/2\). The four-map product construction therefore has Hausdorff dimension
\[
\frac{2\log2}{\log(2/(1-\rho))}.
\]
At \(\rho=1/4\), the exact value is \(2\log2/\log(8/3)\); its decimal approximation \(1.4133901052\) was independently recomputed from the closed form.

Limits: the verification does not establish perturbative persistence, does not give a variable-schedule Hausdorff-dimension formula, and does not perform independent validation.
