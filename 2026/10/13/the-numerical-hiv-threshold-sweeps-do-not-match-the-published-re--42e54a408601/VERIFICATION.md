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
The bundled checker evaluates the source's Example 6.2 reproduction number using exact rational table values.

It verifies
\[
B
=
\frac{N\beta_1\Lambda}{cd}
+
\frac{\beta_2\Lambda}{\delta_I d}
=
\frac{508}{23},
\]
and
\[
\frac{\alpha}{\alpha+\delta_L}=\frac57.
\]

For the Figure 1 setting it verifies
\[
\mathcal R_0(\tau)
=
\frac{444373}{20125}e^{-\tau},
\]
with corrected values approximately \(13.39258876\) and \(3.83704092\).

For the Figure 2 setting it verifies
\[
\mathcal R_0(0.05)\approx3.783306997,
\qquad
\mathcal R_0(0.025)\approx3.810722266,
\]
and proves the derivative with respect to \(\xi\) is negative.

It also verifies the uniform lower bound
\[
\mathcal R_0(\xi)>1
\]
for every \(0\le\xi\le1\) at the Figure 2 delay.

The verification is exact arithmetic plus high-precision evaluation of exponentials; no trajectory simulation is used.
