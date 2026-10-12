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
The published survival function is
\[
S(y)=\frac{1}{-\log(1-\eta)}
\sum_{n\ge1}\frac{\eta^n}{n}
\left(\frac{\lambda}{\lambda+n\theta y}\right)^\lambda.
\]
After factoring \((\lambda/\theta)^\lambda y^{-\lambda}\), expand
\[
\left(1+\frac{\lambda}{n\theta y}\right)^{-\lambda}
=
1-\frac{\lambda^2}{n\theta y}
+O(y^{-2}n^{-2}).
\]
Geometric decay of \(\eta^n\) justifies termwise summation and yields
\[
A=
\frac{(\lambda/\theta)^\lambda\operatorname{Li}_{\lambda+1}(\eta)}
{-\log(1-\eta)},
\qquad
B=
\frac{\lambda^2}{\theta}
\frac{\operatorname{Li}_{\lambda+2}(\eta)}
{\operatorname{Li}_{\lambda+1}(\eta)}.
\]

The bundled checker evaluates the original infinite series numerically and verifies convergence to \(A\), \(-B\), and \(B\) under the three scaled limits used in the finding. It also solves the exact survival equation for upper quantiles and confirms convergence of the additive quantile correction to \(-B/\lambda\).

The numerical replay is not used to infer the asymptotic theorem. The result does not provide a uniform finite-\(y\) error bound.
