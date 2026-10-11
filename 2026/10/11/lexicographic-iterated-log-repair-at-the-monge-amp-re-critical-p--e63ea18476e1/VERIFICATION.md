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

Set
\[
g(t)=t^{1/n}\prod_{j=1}^mL_j(t)^{-\beta_j},
\qquad
q(t)=\frac{tg'(t)}{g(t)}.
\]
Direct logarithmic differentiation gives
\[
q(t)=\frac1n-
\sum_{j=1}^m
\frac{\beta_j}{L_1(t)\cdots L_j(t)}
\longrightarrow\frac1n.
\]
Also
\[
g''(t)=\frac{g(t)}{t^2}
\bigl(q(t)^2-q(t)+tq'(t)\bigr),
\]
and \(tq'(t)\to0\), so the bracket tends to
\[
\frac1{n^2}-\frac1n<0.
\]
This verifies eventual monotonicity and concavity of \(g\), hence monotonicity and convexity of \(\chi(s)=-g(-s)\).

The Monge–Ampère criterion becomes exactly
\[
\int^\infty
q(t)^2
\frac{dt}{t\prod_jL_j(t)^{n\beta_j}}.
\]
Since \(q(t)\to1/n\), successive logarithmic substitutions prove the lexicographic threshold against \((1/n,\ldots,1/n)\), with equality in every coordinate divergent.

The \(W^{1,2}\) criterion becomes
\[
\int^\infty
q(t)^2t^{2/n-2}
\prod_jL_j(t)^{-2\beta_j}\,dt.
\]
For \(n\ge3\), the power exponent is strictly less than \(-1\), so all finite logarithmic factors are harmless.

For \(W^{2,1}\),
\[
\int^\infty g'(t)\,dt=\infty
\]
because \(g(t)\to\infty\). For the distributional Laplacian, \(g'(t)\to0\) and eventual concavity gives
\[
\int^\infty|g''(t)|\,dt<\infty.
\]
Thus the source endpoint criteria give exactly the claimed fixed Sobolev/Laplacian statuses.

No numerical approximation, finite enumeration, or unproved limiting step is used.
