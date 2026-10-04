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
The checker uses exact rational arithmetic only.

It reconstructs exact-line-search steepest descent from
\[
r^{(k)}=b-Ax^{(k)},
\qquad
\alpha_k=
\frac{(r^{(k)})^{\mathsf T}r^{(k)}}
{(r^{(k)})^{\mathsf T}Ar^{(k)}},
\]
and verifies the second-iterate identity used in the proof.

For the diagonal witness
\[
A=\operatorname{diag}(1,2,4),
\qquad
b=(1,1,1/5)^{\mathsf T},
\]
it checks the two exact step lengths, the positive first iterate, the negative third coordinate of the second iterate, and the positive exact solution.

For rational condition numbers larger than \(2\), it checks the closed expression for
\[
\kappa-(\mu_0+\mu_1)
\]
in the three-mode sharpness family and confirms the predicted sign on both sides of the stated \(\varepsilon\) threshold.

For two-dimensional diagonal systems it verifies the two-step residual multiplier and the even/odd iterate formulas over many rational examples. The general Stieltjes and general two-dimensional statements are analytic theorems in RESULT.md, not conclusions from finite enumeration.
