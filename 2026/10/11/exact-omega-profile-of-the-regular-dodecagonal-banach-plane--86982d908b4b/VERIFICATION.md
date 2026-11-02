---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
Let
\[
q=\frac{5-2\sqrt3}{13}.
\]
On the reduced half-edge \(0\le a\le1/2\), define
\[
A(a)=4-\sqrt3+(4\sqrt3-7)a,
\]
\[
C(a)=2\sqrt3-2+(5-3\sqrt3)a,
\]
and
\[
B(a)=
\begin{cases}
4-\sqrt3+(2\sqrt3-4)a,&0\le a\le q,\\
3\sqrt3-3+(7-4\sqrt3)a,&q\le a\le1/2.
\end{cases}
\]
Then
\[
\Phi(a)=\frac{A(a)^2+B(a)^2}{5C(a)^2}.
\]
The exact derivatives are
\[
\Phi'(a)=
\frac{3a(7+4\sqrt3)}{5(4+2\sqrt3-a)^3}
\]
on the first branch and
\[
\Phi'(a)=
\frac{(2+\sqrt3)(a+69+40\sqrt3)}{5(4+2\sqrt3-a)^3}
\]
on the second. Hence the unique half-edge maximum is \(a=1/2\).

At \(a=1/2\),
\[
A=B=\sqrt3+\frac12,
\qquad
C=\frac{1+\sqrt3}{2},
\]
so
\[
\Phi\left(\frac12\right)=\frac{14}{5}-\sqrt3.
\]

The symbolic verifier reconstructs the dodecagonal facets, checks affine dominance at every interval endpoint, proves the derivative identities and verifies the equality pair. The continuum supremum follows from the exact piecewise argument, not finite sampling.
