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
# Exact checks

With \(a=9^{2/3}\) the identity
\[
\bigl(9+3t+3t^2+t^3\bigr)^2-(a+t^2)^3
=54t+(63-3a^2)t^2+36t^3+(15-3a)t^4+6t^5
\]
is strictly positive for every \(t>0\), since \(a^3=81\), \(a<5\), and \(a^2<21\). This proves the lower Hilbert comparison and its exact equality set, with the remaining axis checked directly.

The squared ratio \(R(t)=(8+(1+t)^3)^{2/3}/(a+t^2)\) has derivative sign equal to that of \(a-t(1+8/(1+t)^2)\). The latter decreases strictly, because \(1+8(1-t)/(1+t)^3\ge19/27\); thus it has a single zero \(\tau\). This proves global upper comparison independently of finite sampling.

For any positive quadratic form \(Q\) satisfying \(\alpha Q\le N^2\le\beta Q\), let \(x=(1,0)\) and \(y=(0,\tau)\). Absolute symmetry gives \(N(x+y)^2=N(x-y)^2=N(1,\tau)^2\). The parallelogram identity for \(Q\) then yields \(\beta/\alpha\ge N(1,\tau)^2/(N(x)^2+N(y)^2)=R(\tau)\). The displayed \(H\) attains that ratio. This is a complete universal positive-quadratic-form certificate.

Independent numerical check using high-precision algebraic evaluation: \(\tau\approx2.76673988007870113906853704996\), squared distance \(R(\tau)\approx1.29958204360103898476109693949\), distance \(\sqrt{R(\tau)}\approx1.13999212435921634517891658559\). These decimals are illustrative, not finite-proof substitutes.
