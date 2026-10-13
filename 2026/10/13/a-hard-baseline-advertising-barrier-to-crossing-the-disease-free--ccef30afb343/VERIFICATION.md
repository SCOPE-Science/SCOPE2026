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
The bundled checker uses exact rational arithmetic.

For the source's Table 1 values it verifies
\[
\mathcal R_0=\frac{7500}{4001},
\qquad
c=\lambda_0+d=\frac{201}{25000}.
\]

It checks that
\[
\frac{d\mathcal R_1}{dM_0}
=
-\frac{\mathcal R_0c\lambda p}
{\left(cp+(\lambda+c)M_0\right)^2}
\]
is negative for positive parameters and that
\[
\lim_{M_0\to\infty}\mathcal R_1
=
\frac{\mathcal R_0c}{\lambda+c}.
\]

At the source parameter values it verifies numerically from exact fractions
\[
M_{0,c}\approx1698.1028207,
\]
\[
\mathcal R_1(500)\approx1.3026792112,
\]
and
\[
\lambda_c(500)\approx0.0239061895.
\]

The complete reachability classification is algebraic; no parameter grid is used as proof.
