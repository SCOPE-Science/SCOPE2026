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

Set
\[
r_0=3^{-4/3},
\qquad
F(t)
=
\frac{\bigl(8+(1+t)^3\bigr)^{2/3}}
{4(1+r_0t^2)}.
\]
Then
\[
F(0)=\lim_{t\to\infty}F(t)=\frac{3^{4/3}}4.
\]

The critical equation is
\[
r_0=
\frac{(1+t)^2}{t((1+t)^2+8)}.
\]
The derivative of the right-hand side is
\[
-\frac{(t+1)(t^3+3t^2-5t+9)}
{t^2(t^2+2t+9)^2},
\]
and
\[
t^3+3t^2-5t+9
=
t(t-1)^2+
5\left(t-\frac35\right)^2+
\frac{36}{5}>0.
\]
Hence there is exactly one positive critical point \(\tau\), and it is the global maximum of \(F\).

Therefore
\[
mH(w)^2\le\|w\|_X^2\le MH(w)^2
\]
with
\[
m=\frac{3^{4/3}}4,
\qquad
M=F(\tau).
\]
The Hilbert parallelogram identity gives
\[
C_{\mathrm{NJ}}(X)\le\frac{M}{m}.
\]

For
\[
u=(1,0),
\qquad
v=(0,\tau),
\]
the exact quotient is
\[
\frac{\|u+v\|_X^2+\|u-v\|_X^2}
{2(\|u\|_X^2+\|v\|_X^2)}
=
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}
{3^{4/3}+\tau^2}
=
\frac{M}{m}.
\]
Thus equality holds.

The numerical checks are
\[
\tau=2.76673988007870113906853704996\ldots
\]
and
\[
C_{\mathrm{NJ}}(X)=1.29958204360103898476109693949\ldots .
\]
No finite enumeration, timeout, or numerical optimization establishes the theorem.
