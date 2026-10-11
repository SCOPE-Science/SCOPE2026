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

Normalize
\[
m_0=1,
\qquad
s=m_1,
\qquad
R_W=\sqrt s.
\]

The sharp-radius proof for a non-increasing weight uses the law of
\[
\max(T,s)
\]
as the moment-duality measure. Equality of the two endpoint norms therefore forces equality in every intermediate moment inequality.

The coefficient defect satisfies
\[
X(t)\le\frac{s}{t}Y(t).
\]
The dual measure has positive density on an interval above \(s\), so equality of its integral forces
\[
tX(t)=sY(t)
\]
on an interval. Since \(X\) and \(Y\) are entire in \(t\), the identity holds globally.

Substitution into the source's two-sided circle estimate makes both sides equal. Hence equality holds in the Schwarz--Pick step, and the quotient has the form
\[
\frac fg
=
\frac{az+\eta R_W}
{z+\overline a\,\eta R_W},
\qquad
|a|<1,
\quad
|\eta|=1.
\]

After removing the denominator,
\[
g=(z+\overline a\,\eta R_W)h,
\qquad
f=(az+\eta R_W)h.
\]
For
\[
h(z)=\sum_{j\ge0}c_jz^j,
\]
radial orthogonality gives exactly
\[
\|g\|_W^2-\|f\|_W^2
=
(1-|a|^2)
\sum_{j\ge0}|c_j|^2
(m_{j+1}-R_W^2m_j).
\]

For \(j\ge1\),
\[
m_{j+1}-m_1m_j
=
\frac12
\mathbb E
\left[
(T-T')
(T^j-T'^j)
\right]
>
0,
\]
because \(T\) has an absolutely continuous nondegenerate distribution. Equality therefore forces
\[
h\equiv c.
\]

For the resulting linear pair,
\[
|g(z)|^2-|f(z)|^2
=
|c|^2(1-|a|^2)(|z|^2-R_W^2),
\]
and the norm difference vanishes exactly because
\[
R_W^2m_0=m_1.
\]

All critical steps are exact analytic identities; no numerical certificate is required.
