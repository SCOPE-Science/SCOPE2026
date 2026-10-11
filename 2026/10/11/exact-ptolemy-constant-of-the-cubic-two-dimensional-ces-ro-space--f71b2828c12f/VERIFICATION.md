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
\frac{\left((8+(1+t)^3)/8\right)^{2/3}}
{1+r_0t^2}.
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
t(t-1)^2
+
5\left(t-\frac35\right)^2
+
\frac{36}{5}>0.
\]
Hence there is exactly one positive critical point \(\tau\), and it is the global maximum of \(F\).

The exact parameter satisfies
\[
3^{4/3}(1+\tau)^2
=
\tau((1+\tau)^2+8),
\]
with numerical check
\[
\tau=2.76673988007870113906853704996\ldots .
\]
The global comparison ratio is
\[
\frac{\max F}{\min F}
=
\frac{(8+(1+\tau)^3)^{2/3}}
{3^{4/3}+\tau^2}
=
1.29958204360103898476109693949\ldots .
\]

For
\[
x=(-1,0),\quad y=(0,-\tau),\quad z=(-1,-\tau),
\]
the Ptolemy numerator is \(\|(1,\tau)\|_X^2\), while the denominator is
\[
\|(1,0)\|_X^2+\|(0,\tau)\|_X^2.
\]
These are respectively
\[
\frac{(8+(1+\tau)^3)^{2/3}}4
\]
and
\[
\frac{3^{4/3}+\tau^2}{4}.
\]
Thus the triple attains the global upper bound exactly.

No finite enumeration, timeout, or numerical optimization is used to establish the theorem. The decimal values are consistency checks only.
