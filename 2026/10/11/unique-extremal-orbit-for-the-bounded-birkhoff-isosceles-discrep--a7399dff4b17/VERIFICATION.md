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

The dual norm is
\[
N^*(a,b)=\max\{|a|,|b|,|a+b|\},
\]
hence
\[
\inf_{\lambda\in\mathbb R}N(x+\lambda y)=\frac{|\det(x,y)|}{N(y)}.
\]
After symmetry, \(x=(1,t)\), \(0\le t\le1\), and only three relative unit-edge directions remain.

For \(u=(1-s,-s)\), every nontrivial isosceles case implies \(s+t\le3st\). With \(a=1-s\), \(b=1-t\), \(q=\sqrt{ab}\),
\[
0\le1-2a-2b+3ab\le(1-q)(1-3q),
\]
so \(q\le1/3\) and the determinant is at least \(8/9\), with equality only at \(s=t=2/3\), \(N(y)=1\).

For \(u=(-s,-1)\), every nontrivial case implies \(1-2s-2t+3st\ge0\). With \(q=\sqrt{st}\), the same factor bound gives determinant at least \(8/9\), with equality only at \(s=t=1/3\), \(N(y)=1\).

The isometry \(T(s,t)=(s,s-t)\), together with \(y\mapsto-y\), identifies the two equality chambers. The representative satisfies
\[
N(x)=N(y)=1,\quad N(x+y)=N(x-y)=\frac43,\quad |\det(x,y)|=\frac89.
\]
No numerical optimization establishes the theorem.
