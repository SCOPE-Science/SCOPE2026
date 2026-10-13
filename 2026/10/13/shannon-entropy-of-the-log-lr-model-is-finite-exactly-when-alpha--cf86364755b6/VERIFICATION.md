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
For the Log-LR CDF
\[
G(x)=\left(\frac{\beta}{\beta-\log F_R(x)}\right)^\alpha,
\]
set \(T=-\log F_R(X)\). Then
\[
\Pr(T>t)=\left(\frac{\beta}{\beta+t}\right)^\alpha.
\]
Thus \(T\) is Lomax\((\alpha,\beta)\).

The inverse Rayleigh map is
\[
x(t)=\lambda\sqrt{-2\log(1-e^{-t})},
\]
with
\[
J(t)=\frac{\lambda}{(e^t-1)\sqrt{-2\log(1-e^{-t})}}.
\]
The endpoint expansions are
\[
\log J(t)=-\frac t2+\log\!\left(\frac{\lambda}{\sqrt2}\right)+o(1)
\quad(t\to\infty)
\]
and
\[
\log J(t)=-\log t-\frac12\log\!\bigl(2\log(1/t)\bigr)+O(1)
\quad(t\downarrow0).
\]
The latter is integrable against a bounded density near zero. The former is integrable in the negative tail exactly when \(\mathbb E[T]<\infty\), i.e. \(\alpha>1\). Therefore \(H(X)\) is finite exactly for \(\alpha>1\), and equals \(-\infty\) otherwise.

The bundled checker verifies the CDF transform, the \(-1/2\) log-Jacobian slope, and the explicit finite-regime expectations from the actual package path. Numerical truncations for \(\alpha\le1\) are consistency checks only and do not establish divergence.
