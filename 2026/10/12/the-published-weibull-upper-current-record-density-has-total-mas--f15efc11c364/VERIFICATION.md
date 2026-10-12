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
Let \(t=(x/\lambda)^k\). The Weibull density satisfies \(f(x)\,dx=e^{-t}\,dt\).

The target paper's displayed upper-current-record density is
\[
\widetilde f_{UC_m}(x)=2^m f(x)P(m,t/2).
\]
For integer \(m>1\),
\[
P(m,t/2)=1-e^{-t/2}\sum_{j=0}^{m-1}\frac{(t/2)^j}{j!}.
\]
Therefore
\[
\begin{aligned}
\int_0^\infty \widetilde f_{UC_m}(x)\,dx
&=2^m\left[
1-\sum_{j=0}^{m-1}
\frac{1}{2^j j!}
\int_0^\infty t^j e^{-3t/2}\,dt
\right]\\
&=2^m\left[
1-\sum_{j=0}^{m-1}\frac{2}{3^{j+1}}
\right]\\
&=(2/3)^m.
\end{aligned}
\]
Thus the displayed function is nonnormalized.

The general current-record density printed in the same source is
\[
2^m f(x)
\left[
1-\overline F(x)
\sum_{j=0}^{m-1}
\frac{\{-\log\overline F(x)\}^{j}}{j!}
\right].
\]
With \(\overline F(x)=e^{-t}\), its bracket is \(P(m,t)\). Hence the corrected density is
\[
f_{UC_m}(x)=2^m f(x)P(m,t).
\]

Define
\[
G_m(t)=P(m,2t)-2^m e^{-t}P(m,t).
\]
Using \(P'(m,t)=t^{m-1}e^{-t}/\Gamma(m)\), direct differentiation gives
\[
G_m'(t)=2^m e^{-t}P(m,t).
\]
Also \(G_m(0)=0\) and \(G_m(t)\to1\), so \(G_m((x/\lambda)^k)\) is the corrected CDF.

A separate source check uses the paper's stated \(k=2\) Rayleigh reduction. With \(\lambda=\sqrt{2}\sigma\), the corrected CDF and density coincide exactly with equations (11)-(12) of the author's January 2026 Rayleigh-current-record article. The February formulas do not.

No finite experiment is used as proof. No assertion is made here about the validity of the separately defined joint-record likelihood.
