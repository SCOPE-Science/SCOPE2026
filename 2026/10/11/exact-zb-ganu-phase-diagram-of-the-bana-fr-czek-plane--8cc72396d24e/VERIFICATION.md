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

Write
\[
E(z)=\|z\|_2,\qquad F(z)=\lambda|z_1|,\qquad N_\lambda(z)=\max\{E(z),F(z)\}.
\]
For \(0\le\theta\le1\),
\[
N_\lambda(z)^2
\ge
A_\theta z_1^2+\theta z_2^2,
\qquad
A_\theta=\lambda^2-(\lambda^2-1)\theta.
\]

With
\[
p=x+y,\qquad q=x-y,\qquad D=N_\lambda(x)^2+N_\lambda(y)^2,
\]
the pure branch products satisfy
\[
E(p)E(q)\le D,\qquad F(p)F(q)\le D.
\]
For the mixed branch,
\[
D\ge\frac12\left(A_\theta p_1^2+\theta p_2^2+A_\theta q_1^2+\theta q_2^2\right),
\]
hence
\[
\frac{E(p)F(q)}D
\le
\frac{\lambda}{\sqrt{A_\theta\theta}}.
\]
The same holds with \(p,q\) interchanged.

The quadratic
\[
A_\theta\theta
=
\lambda^2\theta-(\lambda^2-1)\theta^2
\]
has maximum \(1\) on \([0,1]\) when \(1<\lambda\le\sqrt2\). When \(\lambda\ge\sqrt2\), its maximum is
\[
\frac{\lambda^4}{4(\lambda^2-1)}.
\]
This gives the upper bound.

For the first regime,
\[
x=(1,1),\qquad y=(-1,1)
\]
gives ratio \(\lambda\). For the second,
\[
x=\left(1,\sqrt{\lambda^2-1}\right),\qquad
y=\left(-1,\sqrt{\lambda^2-1}\right)
\]
gives ratio
\[
2\sqrt{1-\lambda^{-2}}.
\]

Equality in the low regime forces a horizontal mixed chord, equal Euclidean chord lengths, and Euclidean activity for both vectors. This yields
\[
x=r\cos\alpha(\cos\alpha,\sin\alpha),\qquad
y=r\sin\alpha(-\sin\alpha,\cos\alpha)
\]
with
\[
\arccos(\lambda^{-1})\le\alpha\le\arcsin(\lambda^{-1}).
\]
For \(\lambda>\sqrt2\), equality in the interior convex combination forces both vectors onto the circle--strip transition rays, while equality in the direction step forces the displayed sign-reflected orbit.

No finite enumeration, numerical optimization, or external certificate is used as proof.
