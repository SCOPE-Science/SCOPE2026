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

The low-degree formulas are exact. With
\[
y=(1+x)/2,
\]
\[
Q_2^{(\beta)}(2y-1)
=
y^{\beta+1}
\left(
(\beta+3)y-(\beta+2)
\right),
\]
so its critical point is
\[
y_2=(\beta+1)/(\beta+3)
\]
and its critical amplitude is
\[
A_2
=
\left(
\frac{\beta+1}{\beta+3}
\right)^{\beta+1}.
\]

For
\[
Q_3^{(\beta)},
\]
the first critical point is
\[
y_3
=
\frac{
\beta+2+\sqrt{3(\beta+2)/(\beta+4)}
}{
\beta+5
},
\]
and the corresponding amplitude is
\[
A_3
=
y_3^{\beta+1}
\frac{
\sqrt{3(\beta+2)(\beta+4)}-(\beta+2)
}{
\beta+5
}.
\]

After
\[
t=\sqrt{(\beta+2)/(\beta+4)},
\]
the ratio
\[
R=A_3/A_2
\]
is
\[
R(t)
=
\frac{2t}{\sqrt3+t}
\left[
\frac{
t(1+t^2)
}{
(\sqrt3+t)(\sqrt3t-1)
}
\right]^{(3t^2-1)/(1-t^2)}.
\]
The bracketed factor is greater than one.

Using
\[
\log B>2(B-1)/(B+1)
\]
and
\[
q=\sqrt3\,t,
\]
the derivative of
\[
\log R
\]
has a lower bound whose sign is the opposite of
\[
F(q)
=
q^5+7q^4+8q^3+12q^2-81q-27.
\]
On
\[
1<q<\sqrt3,
\]
\[
F'(q)
=
(q-1)(5q^3+33q^2+57q+81)>0,
\]
but
\[
F(\sqrt3)=72-48\sqrt3<0.
\]
Hence
\[
R
\]
is strictly increasing.

The endpoint checks are
\[
\lim_{\beta\downarrow-1}R(\beta)=1/2
\]
and, by the primary source's boundary discrete theorem,
\[
R(-1/3)>1.
\]
Therefore the equation
\[
R(\beta)=1
\]
has exactly one solution.

High-precision evaluation of that exact equation gives
\[
\beta_*
=
-0.36466584452339080365581021836986159\ldots.
\]
The decimal is not used in the proof of uniqueness.

The position inequality is checked independently from
\[
3(\beta+2)(\beta+3)^2-(\beta-1)^2(\beta+4)
=
2(\beta+1)(\beta+5)^2>0
\]
when
\[
\beta\ge1,
\]
while the unsquared comparison is immediate for
\[
-1<\beta<1.
\]
