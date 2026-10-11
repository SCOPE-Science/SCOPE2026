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
\|(p,q)\|_{X^*}
=
\begin{cases}
\sqrt{p^2+q^2},&pq\ge0,\\
\max\{|p|,|q|\},&pq\le0.
\end{cases}
\]

For a smooth Euclidean-arc point, the exact reverse distance is
\[
\frac1{(\sin\theta+\cos\theta)\max\{\sin\theta,\cos\theta\}}
\ge\frac1{\sqrt2}.
\]

For a smooth taxicab-facet point \(x=(-a,b)\), \(a+b=1\), the unit Birkhoff direction is \((1,1)/\sqrt2\), and
\[
d(x,y)=\frac1{\sqrt2\sqrt{a^2+b^2}}\ge\frac1{\sqrt2}.
\]

At \(x=(1,0)\), every unit Birkhoff direction is
\[
y=\frac{(\tau,1)}{\sqrt{1+\tau^2}},
\qquad0\le\tau\le1,
\]
and
\[
d(x,y)=\frac1{\sqrt{1+\tau^2}}\ge\frac1{\sqrt2}.
\]
Equality occurs at \(\tau=1\), hence \(\varepsilon_D=1/\sqrt2\).

No numerical optimization or finite sampling is used as proof.
