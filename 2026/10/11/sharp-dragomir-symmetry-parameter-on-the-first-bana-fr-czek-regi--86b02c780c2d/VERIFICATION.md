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

Put
\[
\alpha=\lambda^{-1},
\qquad
\beta=\sqrt{1-\alpha^2},
\qquad
\beta\le\alpha.
\]
The unit ball is the Euclidean disk clipped by \(|u|\le\alpha\).

On a circular arc, the forced Birkhoff direction is perpendicular in the Euclidean sense. If its first coordinate does not hit the clip, the reverse distance is \(1\). Otherwise the exact distance is
\[
\frac{\alpha}{s(\alpha s+\beta c)}
\ge
\frac{2\alpha}{1+\alpha}
>
\alpha,
\]
using the largest eigenvalue \((1+\alpha)/2\) of the quadratic form \(\alpha s^2+\beta sc\) on \(s^2+c^2=1\).

On a vertical edge \(x=(\alpha,t)\), the forced unit Birkhoff direction is vertical and
\[
d(x,y)=\frac{\alpha}{\sqrt{\alpha^2+t^2}}\ge\alpha.
\]

At the corner \(x=(\alpha,\beta)\), every Birkhoff direction is
\[
y_r=\frac{(1,-r)}{\sqrt{1+r^2}},
\qquad
r\ge\alpha/\beta,
\]
and the annihilator \((\beta,-\alpha)\) gives
\[
d(x,y_r)=\frac{\beta+\alpha r}{\sqrt{1+r^2}}.
\]
This decreases to \(\alpha\), attained by the endpoint direction \((0,-1)\). Hence the sharp reverse distance is \(\alpha=1/\lambda\), and the least modified-Dragomir parameter is \(\sqrt{1-\lambda^{-2}}\).

All steps are analytic; no finite enumeration or numerical optimization is used as proof.
