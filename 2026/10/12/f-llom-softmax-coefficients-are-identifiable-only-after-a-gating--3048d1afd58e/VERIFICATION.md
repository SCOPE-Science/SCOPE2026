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
For augmented covariates \(\widetilde x=(1,x^\top)^\top\) and gate vectors \(g_m\), the checker evaluates
\[
\pi_m(x)=\frac{e^{\widetilde x^\top g_m}}{\sum_j e^{\widetilde x^\top g_j}}.
\]
It verifies that replacing every \(g_m\) by \(g_m+u\) leaves all probabilities and a representative F-LLoM mixture density unchanged at several covariate and lifetime values.

The analytic converse uses
\[
\log\frac{\pi_m(x)}{\pi_M(x)}=\widetilde x^\top(g_m-g_M).
\]
On an affinely spanning covariate set, equality of the gates therefore identifies every difference \(g_m-g_M\). Setting \(g_M=0\) makes the representation unique.

The checker also applies the source's displayed formula
\[
\operatorname{BIC}=-2\ell+p_M\log n
\]
to the \(n=500\), censoring-rate \(0.10\) row of Table 1. The inferred counts are within table-rounding error of \(3,8,13,18\), exactly the baseline-normalized formula \(3M+2(M-1)\).
