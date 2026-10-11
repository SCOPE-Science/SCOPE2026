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
Set
\[
r=\sqrt2-1,
\qquad
d_0=\frac1{1+r^2}.
\]
The exact simplifications are
\[
d_0=\frac{2+\sqrt2}{4},
\qquad
1-d_0^2=\frac{5-2\sqrt2}{8}.
\]

For an interior point
\[
x=(1,t),
\qquad
-r<t<r,
\]
Birkhoff--James orthogonality forces
\[
y=(0,\pm1),
\]
and
\[
\operatorname{dist}(y,\mathbb Rx)
=
\frac1{1+r|t|}
\ge d_0.
\]

At
\[
x=(1,r),
\]
write the support-kernel direction as
\[
y=\frac{(q,-1)}{N_8(q,-1)},
\qquad
0\le q\le1.
\]
Then
\[
N_8(q,-1)=1
\]
for \(0\le q\le r\), while
\[
N_8(q,-1)=\frac{1+q}{\sqrt2}
\]
for \(r\le q\le1\). The determinant quotient is
\[
\frac{1+rq}{(1+r^2)N_8(q,-1)}.
\]
The first branch is at least \(d_0\) trivially. On the second branch,
\[
\sqrt2(1+rq)-(1+q)=r(1-q)\ge0,
\]
so it is also at least \(d_0\).

The bundled `verify.py` checks these identities symbolically and stress-tests all edge and normal-cone directions numerically. The numerical grid is supplementary; the displayed branch formulas prove the continuum result.

No independent audit or independent validation has been performed.
