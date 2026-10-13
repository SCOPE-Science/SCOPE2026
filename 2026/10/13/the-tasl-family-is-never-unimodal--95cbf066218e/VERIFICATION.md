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
For the published TASL density, define \(q_\alpha=f_\alpha'/f_\alpha\). Direct logarithmic differentiation gives
\[
q_\alpha(x)=
-\frac{2\alpha(1-\alpha x)}{(1-\alpha x)^2+1}
+\frac{4x(x^2-1)}{(x^2-1)^2+2}
-\tanh(x/2).
\]

For \(\alpha>0\),
\[
q_\alpha(0)=-\alpha<0,
\qquad
q_\alpha(-\infty)=1,
\qquad
q_\alpha(+\infty)=-1.
\]
At \(x=2\), setting \(y=1-2\alpha<1\) reduces the parameter-dependent term to
\[
\frac{y^2-y}{y^2+1}.
\]
Its derivative has numerator \(y^2+2y-1\), so its minimum on \(y<1\) occurs at \(y=\sqrt2-1\) and equals \((1-\sqrt2)/2\). Hence
\[
q_\alpha(2)
\ge \frac{1-\sqrt2}{2}+\frac{24}{11}-\tanh(1)
> \frac{37-11\sqrt2}{22}>0.
\]

The sign sequence therefore forces a strict local maximum to the left of \(0\) and another to the right of \(2\), with a local minimum between them. The reflection identity \(f_\alpha(x)=f_{-\alpha}(-x)\) handles negative \(\alpha\). At \(\alpha=0\), evenness plus \(q_0(2)>0\) and \(q_0(+\infty)=-1\) gives symmetric outer local maxima.

Scientific limit: this verifies that at least two modes exist for every real parameter. It does not determine the exact parameter threshold between two and three modes.
