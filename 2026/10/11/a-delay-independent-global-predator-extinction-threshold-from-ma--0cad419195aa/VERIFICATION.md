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

# Verification

The printed denominator factors as
\[
1+b_1P_1+kb_3P_3+kb_1b_3P_1P_3=(1+b_1P_1)(1+kb_3P_3).
\]

With
\[
a=\frac{c_2}{d_2+c_2},\qquad
L=aP_2+P_3+c_2\int_{t-\tau_2}^{t}P_2(s)\,ds,
\]
direct differentiation gives
\[
\dot L=
a\eta b_2\frac{P_1P_3}{(1+b_1P_1)(1+kb_3P_3)}
-d_3P_3-c_3P_3^2.
\]
The checker verifies the cancellation coefficients symbolically.

It also verifies
\[
(d_2+c_2)d_3-
\frac{\eta c_2b_2(r-d_1)}{c_1+b_1(r-d_1)}
=(d_2+c_2)d_3\bigl(1-\mathcal R_{\mathrm{mat}}\bigr),
\]
so the theorem's strict threshold is exactly the source's strict undelayed local-stability inequality.

At the illustrative coefficients, exact rational arithmetic gives
\[
\mathcal R_{\mathrm{mat}}=\frac{928}{93}\eta,
\]
hence \(\eta<93/928\), while the source's simpler sufficient condition gives \(\eta<1/12\).

The analytic proof does not rely on numerical integration, finite-time experiments, or a local linearization. The threshold equality and superthreshold dynamics are unproved here.
