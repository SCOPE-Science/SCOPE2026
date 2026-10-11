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

For every \(2<p<\infty\), set
\[
\tau=2^{-2/p}.
\]
After coordinate-swap averaging, every Euclidean pullback relevant to the infimum can be written, up to scale, as
\[
E_t^2=(x+y)^2+t(x-y)^2.
\]

On the same-sign sector, with \(r=|x-y|/|x+y|\),
\[
R_p(r;t)=
\frac{4(1+tr^2)}
{\bigl((1+r)^p+(1-r)^p\bigr)^{2/p}}.
\]
On the opposite-sign sector, with \(s=|x+y|/|x-y|\),
\[
R_\infty(s;t)=\frac{4(s^2+t)}{(1+s)^2}.
\]

At \(t=\tau\),
\[
\min_{0\le s\le1}R_\infty(s;\tau)
=\frac{4\tau}{1+\tau},
\qquad
\max_{0\le s\le1}R_\infty(s;\tau)
=4\tau.
\]
For \(p\ge2\),
\[
2^{2/p}(1+r^2)
\le
\bigl((1+r)^p+(1-r)^p\bigr)^{2/p}
\le
2(1+r^2),
\]
which gives
\[
\frac{4\tau}{1+\tau}
<
1+\tau
\le
R_p(r;\tau)
\le
4\tau.
\]
Hence the displayed ellipse has squared distortion \(1+\tau\).

For arbitrary \(0<t\le1\),
\[
\min_sR_\infty(s;t)=\frac{4t}{1+t},
\]
while
\[
R_\infty(0;t)=4t,\qquad R_p(0;t)=4\tau.
\]
Thus the squared distortion is at least
\[
\frac{\max\{4t,4\tau\}}{4t/(1+t)}
\ge1+\tau.
\]
For \(t\ge1\), the two endpoint values of \(R_\infty\) already force distortion at least
\[
\frac{4t}{1+t}\ge2>1+\tau.
\]
This proves the exact global value.

Representative checks:
\[
p=3:\qquad 1+2^{-2/3}=1.6299605249\ldots,
\]
\[
p=4:\qquad 1+2^{-1/2}=1.7071067811\ldots.
\]
No finite sample is used to establish the quantified theorem. The unresolved scope is \(1\le p<2\) and more general Day--James pairs.
