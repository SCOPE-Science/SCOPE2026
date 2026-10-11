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

For a unit Birkhoff--James orthogonal pair in real \(\ell_4^2\), write
\[
A=x_1^2y_1^2+x_2^2y_2^2,
\qquad
B=x_1y_1^3+x_2y_2^3.
\]
Direct parametrization by
\[
x=(a,b),
\qquad
y=\frac{(b^3,-a^3)}{(a^{12}+b^{12})^{1/4}}
\]
gives
\[
B^2=A(1-A^2)
\]
and shows that \(A\) ranges over \([0,1]\).

After choosing the minimizing sign,
\[
\|x+\lambda y\|_4^4
=
1+\lambda^4+6A\lambda^2
-4\lambda^3\sqrt{A(1-A^2)}.
\]
For each \(\lambda>0\), the unique minimizing \(A\) satisfies
\[
\lambda(1-3A^2)=3\sqrt{A(1-A^2)}.
\]
At a stationary point of the remaining one-variable objective,
\[
\lambda=
\frac{9A^4-12A^2+1}{3A(1-3A^2)}.
\]
The first right-hand side obtained from the denominator minimization is strictly increasing in \(A\); this second one is strictly decreasing wherever it is positive. Hence there is exactly one critical point.

On their positive common interval, squaring their equality gives
\[
81A^8-216A^6+81A^5+162A^4-81A^3-24A^2+1=0.
\]
The unique admissible root is
\[
A_*=0.174177500540137295788576370582\ldots,
\]
which gives
\[
\lambda_*=1.35634457846695755421350607134\ldots
\]
and
\[
\mu(\ell_4^2)=1.93365718463403520398276193150\ldots.
\]
The final decimal rounds to the published numerical benchmark \(1.9337\).

The proof of uniqueness is analytic and precedes numerical evaluation. Finite sampling and polynomial root lists are not used as proof.
