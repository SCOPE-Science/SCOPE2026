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
For one parent-Shanker observation \(T\),
\[
\ell(\alpha;T)
=
2\log\alpha-\log(\alpha^2+1)+\log(\alpha+T)-\alpha T.
\]
Thus
\[
-\ell''(\alpha;T)
=
\frac{2}{\alpha^2}
+\frac{2(1-\alpha^2)}{(\alpha^2+1)^2}
+\frac{1}{(\alpha+T)^2}.
\]
The expectation of the final term is
\[
\frac{\alpha^2}{\alpha^2+1}
\int_0^\infty \frac{e^{-\alpha t}}{\alpha+t}\,dt
=
\frac{\alpha^2}{\alpha^2+1}
e^{\alpha^2}E_1(\alpha^2).
\]
This yields the Fisher-information formula used in the finding.

The bundled checker evaluates the defining expectation numerically and verifies agreement with the closed form at multiple parameter values. It also verifies the endpoint-scaled ratios used to distinguish the true Jeffreys-rule prior from \(1/\alpha\).

For the source's log-uniform kernel, the posterior behaves as \(O(\alpha^{2n-1})\) at zero and as
\[
O\!\left(\alpha^{n-1}e^{-\alpha\sum_i x_i/(1-x_i)}\right)
\]
at infinity. Both tails are integrable for every \(n\ge1\) and every \(0<x_i<1\).

No simulation table or posterior summary from the source is recomputed here.
