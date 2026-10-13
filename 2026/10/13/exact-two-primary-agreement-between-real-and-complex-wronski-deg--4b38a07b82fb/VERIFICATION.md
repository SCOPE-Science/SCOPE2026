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
Let
\[
D_{\mathbb C}(a,b)
=
\frac{1!2!\cdots(b-1)!\,(ab)!}{a!(a+1)!\cdots(a+b-1)!}
\]
and use the explicit nonzero real-degree product
\[
D_{\mathbb R}(a,b)
\]
from the rectangular sign-imbalance formula.

For
\[
F(n)=\nu_2(n!),
\qquad
M=ab/2,
\qquad
L=(a-b+1)/2,
\qquad
U=(a+b-1)/2,
\]
direct cancellation gives
\[
\nu_2(D_{\mathbb C})-\nu_2(D_{\mathbb R})
=
F(2M)-F(M)-\sum_{t=L}^{U}\bigl(F(2t)-F(t)\bigr).
\]
Because
\[
F(2t)-F(t)=t
\]
and
\[
\sum_{t=L}^{U}t=ab/2=M,
\]
the difference is zero.

Legendre's formula then yields
\[
\nu_2(D_{\mathbb C})
=
\sum_{j=0}^{b-1}s_2(a+j)
-
\sum_{j=1}^{b-1}s_2(j)
-
s_2(ab).
\]

The bundled checker evaluates both exact factorial formulas for all opposite-parity pairs with
\[
2\le b\le a\le120
\]
and checks the Catalan specialization through \(a=399\). These finite computations are regression evidence only.
