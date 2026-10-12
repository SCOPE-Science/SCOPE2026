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
The exact APIILx survival is
\[
S(x)=\frac{2^\alpha-[2-v(x)]^\alpha}{2^\alpha-1},
\qquad
v(x)=\left(\frac{\lambda}{\lambda+x}\right)^\theta.
\]
Expanding at \(v=0\) gives
\[
S(x)=\frac{\alpha2^{\alpha-1}}{2^\alpha-1}v(x)
\left[1-\frac{\alpha-1}{4}v(x)+O(v(x)^2)\right].
\]
Thus \(S(x)\asymp x^{-\theta}\) and \(f(x)\asymp x^{-\theta-1}\) on the terminal tail. These two-sided comparisons are enough to prove all integrability statements without numerical extrapolation.

For every real \(q>0\),
\[
\mathbb E[X^q]=q\int_0^\infty x^{q-1}S(x)\,dx
\]
when finite, and the tail integrand is comparable to \(x^{q-\theta-1}\). Therefore the exact threshold is \(q<\theta\).

For every \(t>0\), the lower comparison \(f(x)\ge c x^{-\theta-1}\) for sufficiently large \(x\) implies
\[
\mathbb E[e^{tX}]=\infty.
\]
The bundled checker evaluates the exact model at finite points only to replay the constants and signs; it is not evidence for an infinite-domain conclusion.
