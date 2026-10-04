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
The general statement is verified analytically from the printed equilibrium coefficients.

Critical proof checks:
- The disease-free coordinates give
  \[
  R_{\mathrm{vac}}=
  \frac{\beta\Lambda(a+r\gamma)}{dm(a+\gamma)}.
  \]
- If \(R_{\mathrm{vac}}\le1\), then
  \[
  \frac{\Lambda\beta r}{m}
  \le d\frac{r(a+\gamma)}{a+r\gamma}
  \le d.
  \]
- Substitution in the printed coefficient gives \(B_1<0\), including the boundary \(r=0\), \(\delta=0\).
- For \(R_{\mathrm{vac}}<1\), no positive root exists.
- For \(R_{\mathrm{vac}}=1\), the constant term vanishes and the remaining factor is negative for positive \(I\).
- For \(R_{\mathrm{vac}}>1\), exactly one positive root exists by opposite root signs when \(r>0\), or by the linear equation when \(r=0\).

`verify.py` uses exact rational arithmetic to replay the coefficient formulas over boundary and interior parameter cases. It also reconstructs the source's disease-free numerical example and obtains \(R_{\mathrm{vac}}\approx0.8016\).

Finite replay is supporting evidence only; it is not used to infer the all-parameter theorem.

No independent audit has been performed.
