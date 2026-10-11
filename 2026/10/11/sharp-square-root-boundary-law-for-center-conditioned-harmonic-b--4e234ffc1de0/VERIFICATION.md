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

For bounded harmonic \(f=P[F]\) with \(|F|\le1\) and \(|c_0|=a\), Parseval gives
\[
\sum_{n\ne0}|c_n|^2\le1-a^2.
\]
Cauchy--Schwarz with weights \(r^{|n|}\) gives
\[
B_f(r)-a\le \sqrt{1-a^2}\left(2\sum_{n\ge1}r^{2n}\right)^{1/2}
=\sqrt{2(1-a^2)}\frac{r}{\sqrt{1-r^2}}.
\]
Solving \(B_f(r)\le1\) yields
\[
r^2\le\frac{1-a}{3+a}.
\]
This proves the uniform bound for all admissible functions, not just finitely many coefficient samples.

For the explicit smooth unimodular trace
\[
F_\varepsilon(e^{it})=e^{i\varepsilon\cos t},
\]
Fourier integration and parity give
\[
c_0=1-\frac{\varepsilon^2}{4}+O(\varepsilon^4),
\qquad
c_1=c_{-1}=\frac{i\varepsilon}{2}+O(\varepsilon^3).
\]
The Poisson extension is bounded by one. Thus, with \(a=c_0\) for sufficiently small positive \(\varepsilon\), its majorant fails whenever
\[
r>\frac{1-a}{|c_1|+|c_{-1}|}
=\left(\frac12+o(1)\right)\sqrt{1-a}.
\]
The Taylor derivative \(c_0'(\varepsilon)=-\varepsilon/2+O(\varepsilon^3)<0\) shows that the witness covers every center value close enough to one. Together with the universal lower bound, this proves
\[
\lim_{a\uparrow1}\frac{R_H(a)}{\sqrt{1-a}}=\frac12.
\]
The source formula is strictly smaller for every \(a<1\), since, with \(t=1-a\),
\[
(t+4/\pi)^2>(t+1)^2>t(4-t).
\]
Finally, the maximum principle forces every map with \(|f(0)|=1\) to be constant, so \(R_H(1)=1\).

Consistency checks evaluated the exact special-function integrals at several small positive parameters and confirmed convergence of the normalized lower and witness upper bounds to \(1/2\). These checks are not used as an infinite proof. The exact \(R_H(a)\) for fixed \(a<1\) remains unresolved here.
