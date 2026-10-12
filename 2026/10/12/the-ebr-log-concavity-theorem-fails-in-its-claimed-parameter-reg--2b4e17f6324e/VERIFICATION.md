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
With
\[
x=t/\alpha,\qquad
G(x)=1-e^{-x^2/2},\qquad
H(x)=G(x)^\beta,
\]
the exact source density has log
\[
\ell(t)
=
C+\log x-\frac{x^2}{2}
+(\beta-1)\log G(x)
-\lambda H(x)
-e^\lambda\{1-e^{-\lambda H(x)}\}.
\]

The origin expansion proves, for \(\beta\ne1/2\),
\[
\ell''(t)
=
-\frac{2\beta-1}{t^2}+o(t^{-2}).
\]
At \(\beta=1/2\),
\[
\lim_{t\downarrow0}\ell''(t)
=
\frac1{\alpha^2}
\left(
\frac{\lambda^2e^\lambda}{2}-\frac34
\right).
\]

At \(\beta=1\) and \(t=\alpha\),
\[
\ell''(\alpha)
=
\frac1{\alpha^2}
\left[
\lambda^2e^{-1+\lambda e^{-1/2}}-2
\right].
\]

The bundled checker evaluates the exact log-density by high-precision differentiation, checks the origin asymptotic, computes both unique positive roots, and confirms the explicit counterexample \((\alpha,\beta,\lambda,t)=(1,1,2,1)\).
