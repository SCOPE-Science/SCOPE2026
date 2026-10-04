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
The analytic identification is
\[
dK_t=(A-\delta K_t)\,dt+\sigma\sqrt{K_t}\,dW_t
=
\delta\left(\frac{A}{\delta}-K_t\right)dt
+\sigma\sqrt{K_t}\,dW_t.
\]
Thus the source state process is a CIR square-root diffusion.

For \(t>0\),
\[
K_t\overset{d}=c_tY_t,
\qquad
c_t=\frac{\sigma^2(1-e^{-\delta t})}{4\delta},
\]
where \(Y_t\) is noncentral chi-square with
\[
\nu=\frac{4A}{\sigma^2},
\qquad
\lambda_t=
\frac{4\delta e^{-\delta t}K_0}
{\sigma^2(1-e^{-\delta t})}.
\]

At stationarity,
\[
K_\infty\sim
\Gamma\!\left(
\frac{2A}{\sigma^2},
\frac{\sigma^2}{2\delta}
\right).
\]

The bundled checker replays the source's Nash parameters and verifies
\[
X_N^*=2.4,\quad
Y_N^*=1.6,\quad
A_N=2.4,\quad
K_\infty\sim\Gamma(30,0.8).
\]
It independently evaluates the regularized Gamma distribution to reproduce:
\[
[16.19269922,33.31906995]
\]
for the exact stationary equal-tail 95% interval,
\[
[-13.632,61.632]
\]
for the source's printed limiting band, and approximately
\[
0.999999999676
\]
for the exact stationary coverage of that printed band.

The finite-time and stationary distribution statements are analytic and are not inferred from numerical simulation.
