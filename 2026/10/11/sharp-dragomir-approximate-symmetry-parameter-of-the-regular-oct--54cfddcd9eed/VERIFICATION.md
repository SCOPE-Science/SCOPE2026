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

Let
\[
a=\sqrt2-1.
\]
The dual norm is
\[
N^*(p,q)=\max\{|p|+a|q|,\ a|p|+|q|\}.
\]

For a smooth edge point \(x_t=(1,t)\), \(0\le t<a\), the unit Birkhoff direction is \(y=(0,1)\). The annihilator \((-t,1)\) has dual norm \(1+at\), and an explicit translate attains
\[
d(x_t,y)=\frac1{1+at}.
\]

At the vertex \(x=(1,a)\), all Birkhoff directions are \(y_r=(r,-1)/m(r)\), \(0\le r\le1\), with
\[
m(r)=
\begin{cases}
1,&r\le a,\\
(1+r)/\sqrt2,&r\ge a.
\end{cases}
\]
The annihilator \((-a,1)\) has dual norm \(1+a^2\), and an explicit translate attains
\[
d(x,y_r)=\frac{1+ar}{m(r)(1+a^2)}.
\]
This increases on \([0,a]\) and decreases on \([a,1]\), giving the minimum
\[
\frac1{1+a^2}=\frac{2+\sqrt2}{4}.
\]

Therefore
\[
\varepsilon_D^2
=
1-\left(\frac{2+\sqrt2}{4}\right)^2
=
\frac{5-2\sqrt2}{8}.
\]
No numerical optimization or finite sampling is used as proof.
