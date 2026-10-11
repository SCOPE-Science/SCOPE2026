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
N^*(a,b)=
\begin{cases}
|a|+|b|,&ab\ge0,\\
\sqrt{a^2+b^2},&ab\le0.
\end{cases}
\]

For a smooth square-edge point \(x=(1,t)\), \(0<t<1\), the forced unit Birkhoff direction is \(y=(0,1)\), and
\[
d(x,y)=\frac1{\sqrt{1+t^2}}\ge\frac1{\sqrt2}.
\]

For a smooth circular-arc point \(x=(c,-s)\), \(c^2+s^2=1\), \(c\ge s>0\), put \(r=s/c\). The forced unit Birkhoff direction is \(y=(s/c,1)\), and
\[
d(x,y)=\frac{1+r^2}{1+r}\ge2(\sqrt2-1)>\frac1{\sqrt2}.
\]

At the square corner \(x=(1,1)\), every unit Birkhoff direction is an opposite-sign Euclidean unit vector \(y=(c,-s)\). Then
\[
d(x,y)=\frac{c+s}{\sqrt2}\ge\frac1{\sqrt2},
\]
with equality at a coordinate axis.

Therefore
\[
\inf_{\substack{x,y\in S_X\\x\perp_B y}}d(x,y)=\frac1{\sqrt2},
\qquad
\varepsilon_D(X)=\frac1{\sqrt2}.
\]

No numerical optimization, sampling, or external certificate is used as proof.
