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
The bundled `verify.py` uses only the Python standard library.

It verifies the Case 2 lower prey-mean bound
\[
1-\frac15\left(\frac25+1\right)=\frac{18}{25},
\]
and expands the second mean constraint after multiplication by the positive denominator \(3/5+\bar u\). The boundary polynomial is proportional to
\[
-875\bar u^2+290\bar u+399,
\]
whose positive zero is
\[
\frac{29+\sqrt{14806}}{175}.
\]

It verifies the source Case 2 coexistence coefficients
\[
A=-\frac{11}{50},\qquad B=-\frac{133}{250},
\]
so the positive root of \(u^2+Au+B=0\) is
\[
\frac{11+\sqrt{5441}}{100}.
\]

It also checks, at exact rational synthetic moments, the algebraic identity
\[
q\frac{1-\bar u}{s}
+\frac{\bar u(1-\bar u)-\operatorname{Var}_T(u)}s
=
\frac{(q+\bar u)(1-\bar u)-\operatorname{Var}_T(u)}s.
\]

The stored checker output is `VERIFY_OK`.

The strict inequalities and all-parameter theorem are analytic consequences of positivity, period-shift invariance, and Jensen's inequality. They are not inferred from finite simulation. The verification does not establish existence or stability of periodic solutions.
