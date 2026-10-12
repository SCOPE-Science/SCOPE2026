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
The source defines
\[
J_\beta(u)=\frac{[-\log(1-u)]^{\beta-1}}{\Gamma(\beta+1)}[\beta+1+\log(1-u)]
\]
only for \(0<u<1\), then defines the empirical statistic using \(J_\beta(i/n)\) for \(i=1,\ldots,n\).

Set \(v=-\log(1-u)\). Then
\[
J_\beta(u)=\frac{v^{\beta-1}(\beta+1-v)}{\Gamma(\beta+1)}
=-\frac{v^\beta}{\Gamma(\beta+1)}\left(1-\frac{\beta+1}{v}\right),
\]
so \(J_\beta(u)\to-\infty\) as \(u\uparrow1\) for every \(\beta>0\).

Therefore the printed term with \(i=n\) is undefined. Under the exponential null, \(X_{(n)}>0\) almost surely, so the left-limit extension would force the whole empirical statistic to \(-\infty\), not a finite random variable.

The source's spacing coefficient
\[
b_{r,n}=\frac1{n-r+1}\sum_{i=r}^nJ_\beta(i/n)
\]
contains the same endpoint term for every \(r\). Hence the finite coefficients assumed by the exact-null product formula are not present in the printed definition.

For the monotonicity check,
\[
\frac{dJ_\beta}{dv}=\frac{v^{\beta-2}}{\Gamma(\beta+1)}(\beta^2-1-\beta v).
\]
Thus \(J_\beta\) is not monotone for \(\beta>1\). This independently invalidates the all-\(\beta\) monotonicity justification in Remark 3.1.

No numerical experiment is needed. The conclusion is limited to the formulas as printed and does not assess an unstated regularized implementation.
