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

For \(0\le t\le1\),
\[
Q_\lambda(t)
=
\frac{\lambda+(1+t)^2}{1+t^2},
\qquad
Q_\lambda'(t)
=
\frac{2(1-\lambda t-t^2)}{(1+t^2)^2}.
\]
The unique critical point is
\[
t_\lambda=\frac{\sqrt{\lambda^2+4}-\lambda}{2},
\]
and it is the global maximum. The value is
\[
M_\lambda=\frac{\lambda+2+\sqrt{\lambda^2+4}}2.
\]
The endpoint values are
\[
Q_\lambda(0)=1+\lambda,
\qquad
Q_\lambda(1)=\frac{\lambda+4}{2},
\]
so
\[
m_\lambda=
\begin{cases}
1+\lambda,&0<\lambda\le2,\\
(\lambda+4)/2,&\lambda\ge2.
\end{cases}
\]
Thus \(C_{\mathrm{Pt}}\le M_\lambda/m_\lambda\).

For \(0<\lambda\le2\), choose
\[
x=(1,0),\quad y=(0,t_\lambda),\quad z=(1,t_\lambda).
\]
Then the denominator is
\[
m_\lambda(1+t_\lambda^2),
\]
and the numerator is
\[
M_\lambda(1+t_\lambda^2),
\]
so the exact ratio is \(M_\lambda/m_\lambda\).

For \(\lambda>2\), choose
\[
x=(1+t_\lambda,1+t_\lambda),
\quad
y=(1-t_\lambda,-(1-t_\lambda)),
\quad
z=(2,2t_\lambda).
\]
The numerator is
\[
4M_\lambda(1+t_\lambda^2),
\]
and the denominator is
\[
4m_\lambda(1+t_\lambda^2),
\]
again giving the exact ratio.

For Euclidean Banach--Mazur distance, average an arbitrary positive-definite quadratic pullback over all coordinate sign changes and the coordinate swap. The comparison bounds are preserved, while the averaged form is necessarily a scalar multiple of \(x^2+y^2\). Hence no ellipse improves the Euclidean comparison, and
\[
d_{\mathrm{BM}}^2=M_\lambda/m_\lambda.
\]

The published formula for \(C_{\mathrm{NJ}}(Z_{1,\infty})\) is the same piecewise value. No finite enumeration or numerical optimization establishes any part of the theorem.
