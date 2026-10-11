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
For \(x\in S_{c_0(I)}\), fix \(k\) with \(|x_k|=1\) and set \(s=s_2(x)\). Given arbitrary \(y\in S_{c_0(I)}\), choose a sign \(\sigma\) with
\[
|x_k+\sigma y_k|\le1.
\]
Then
\[
\|x+\sigma y\|_\infty\le1+s,
\qquad
\|x-\sigma y\|_\infty\le2.
\]
Coordinatewise monotonicity of \(M_t\) therefore proves the upper bound for every parameter in the defining scale.

For \(s>0\), choose \(l\ne k\) with \(|x_l|=s\) and take the two-coordinate witness
\[
y_k=\operatorname{sgn}(x_k),
\qquad
y_l=-\operatorname{sgn}(x_l).
\]
For \(s=0\), use any \(l\ne k\) with \(y_l=1\). In both cases,
\[
\|x+y\|_\infty=2,
\qquad
\|x-y\|_\infty=1+s
\]
after the harmless choice of the displayed signs.

The bundled checker tests the upper bound on a deterministic rational finite-support grid and checks the equality witness for negative, zero, and positive parameters. These checks are supplemental; the displayed coordinate argument proves the full infinite-dimensional theorem.

No independent audit or independent validation has been performed.
