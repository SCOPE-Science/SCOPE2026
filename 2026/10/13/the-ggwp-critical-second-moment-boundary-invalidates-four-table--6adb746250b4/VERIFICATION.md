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
The source proves
\[
\Pr(T>t)\sim C t^{-1/\beta},
\qquad
C=
\frac{a e^{-1/b}}{b(1-e^{-1/b})}\theta^{1/\beta}>0.
\]
For a nonnegative variable,
\[
\mathbb E[T^r]
=
r\int_0^\infty t^{r-1}\Pr(T>t)\,dt.
\]
Thus at the critical equality
\[
r=1/\beta
\]
the integrand is asymptotic to
\[
rC/t,
\]
which gives logarithmic divergence.

For \(\beta=1/2\), this proves
\[
\mathbb E[T]<\infty,
\qquad
\mathbb E[T^2]=\infty.
\]
Hence variance, coefficient of variation, standardized skewness, and standardized kurtosis cannot be finite population summaries.

The bundled checker evaluates the exact GGWP survival from the published CDF for the four affected Table 1 parameter rows and confirms
\[
t^2\Pr(T>t)\to C.
\]
It also reports the positive logarithmic-divergence coefficient \(2C\). These finite calculations are consistency checks only.
