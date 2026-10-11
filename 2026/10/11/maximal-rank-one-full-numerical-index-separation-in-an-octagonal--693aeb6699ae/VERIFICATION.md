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

The source formulas are
\[
n(X_\xi)=
\max\left\{\xi,\frac{1-\xi}{1+\xi}\right\}
\]
and the four-branch expression for \(n_1(X_\xi)\) reproduced in the result.

Let
\[
a=\sqrt5-2,\qquad b=\sqrt2-1,\qquad c=\frac{\sqrt5-1}{2}.
\]
The quotient is identically \(1\) on \([0,a]\cup[c,1]\).

For \(a<\xi<b\), exact differentiation yields
\[
R_-'(\xi)=
\frac{2A_-(\xi)}
{\sqrt{Q_-(\xi)}(1-\xi)^2(2+\xi-\xi^2+\sqrt{Q_-(\xi)})^2}.
\]
The denominator is positive. The polynomial component satisfies
\[
P_-'(\xi)\ge12,
\qquad
P_-(a)=16(263\sqrt5-588)>0,
\]
and the remaining radical contribution to \(A_-\) is positive. Therefore \(R_-'(\xi)>0\).

For \(b<\xi<c\),
\[
R_+'(\xi)=
\frac{2A_+(\xi)}
{\sqrt{Q_+(\xi)}\,\xi^2(1+3\xi+\sqrt{Q_+(\xi)})^2}.
\]
Again the denominator is positive. Here \(P_+''(\xi)>0\), while
\[
P_+(b)=416-296\sqrt2<0,
\qquad
P_+(c)=32-15\sqrt5<0.
\]
Thus \(P_+<0\) throughout the interval, and the radical contribution to \(A_+\) is also negative. Hence \(R_+'(\xi)<0\).

Finally,
\[
R(b)=
\frac{4}{3-\sqrt2+\sqrt{10\sqrt2-13}}
=
1.506878584864220\ldots,
\]
and \(1+b=\sqrt2\), so \(X_b\) is the regular octagonal plane.

The derivative identities and exact endpoint simplifications were independently recomputed symbolically. The proof itself uses the displayed exact algebraic identities and sign arguments; finite sampling is not evidentiary.
