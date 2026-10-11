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

For
\[
H_t(x,y)^2=(x+y)^2+t(x-y)^2,
\]
the same-sign sector has
\[
R_1(s;t)=1+ts^2,\qquad 0\le s\le1.
\]
On the opposite-sign sector,
\[
u=\left(\frac{|x+y|}{|x-y|}\right)^2\in[0,1]
\]
and
\[
R_3(u;t)=2^{4/3}\frac{t+u}{(1+3u)^{2/3}},
\qquad
\frac{\partial}{\partial u}\log R_3(u;t)
=
\frac{1+u-2t}{(t+u)(1+3u)}.
\]

For \(0<t\le1/2\),
\[
D(t)=
\begin{cases}
\dfrac{1+t}{2^{4/3}t},&0<t\le2^{-4/3},\\[2mm]
1+t,&2^{-4/3}\le t\le1/2.
\end{cases}
\]
The first branch decreases and the second increases. For \(t\ge1/2\), same-sign contacts give \(D(t)\ge1+t\ge3/2\). Therefore
\[
\min_{t>0}D(t)=1+2^{-4/3}.
\]
At the optimum the minimum comparison value is \(1\) and the maximum is \(1+2^{-4/3}\), giving
\[
d_{\mathrm{BM}}(X,\ell_2^2)
=
\sqrt{1+2^{-4/3}}
=
1.181884200331001\ldots .
\]

No finite enumeration or numerical optimization establishes the theorem. The unresolved mathematical scope is the general \(\ell_1-\ell_p\) family outside \(p=3\).
