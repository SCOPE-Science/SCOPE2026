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
For \(0<r\le\rho\), the six-vertex reduction gives
\[
M_r(t)
=
\max\left\{
1+(r+t)^4,\,
(1+rt)^4+\max\{r,t\}^4
\right\}.
\]

The first scalar branch has derivative sign
\[
1-r t^3-\left(\frac{t}{r+t}\right)^3.
\]
Its value at \(t=1\) changes sign exactly at
\[
r^3+2r^2-2=0.
\]

For the competing branch on \(t\ge r\), the derivative sign is
\[
t^3+(r-t^3)(1+rt)^3.
\]
The zero equation is equivalent to
\[
t^3\left(1-(1+rt)^{-3}\right)=r.
\]
The left side is strictly increasing, so the critical point is unique.

On \(0\le t\le r\), differentiation gives
\[
(1+rt)^3(r-t^3)-r^4t^3>0
\]
throughout the accepted parameter range, so no earlier maximum is missed.

The bundled `verify.py` enumerates all vertex pairs and replays the scalar phase transition numerically on dense grids. These finite checks are supplementary only; the continuum proof is analytic.

No independent audit or independent validation has been performed.
